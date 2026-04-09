# Cargamos librerías principales
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Match Predictor Premier League",
    page_icon="⚽",
    layout="wide"
)

# Cargamos el modelo 1 (Regresión Logística)
with open('modelLR_v1.pkl', 'rb') as f:
    bundle = pickle.load(f)

model_1 = bundle['modelo']
variables_1 = bundle['features']
objetivo_1 = bundle['target_encoder']
min_max_scaler_1 = bundle['scaler']

# Cargamos el modelo 2
with open('modelTree_2_v1.pkl', 'rb') as f:
    bundle_2 = pickle.load(f)

model_2 = bundle_2['modelo']
variables_2 = bundle_2['features']
objetivo_2 = bundle_2['target_encoder']

# Cargamos los datos preparados para predicción
data_preparada = pd.read_csv('data_preparada.csv')

# El data set se entreno con los datos desde la temporada 2020 - 2021 iniciada - 2020-09-12 hasta la temporada 2025 - 2026 (2026-03-16), exactamente en la Jornada 31 
# Para un total de 1821 partidos

vars1 = ['HomeTeam', 'AwayTeam','Year', 'Month', 'DayOfWeek', 'B365H', 'B365D', 'B365A', 'BWH', 'BWD', 'BWA', 'B365>2.5', 'B365<2.5',
       'AHh', 'B365CH', 'B365CD', 'B365CA', 'BWCH', 'BWCD', 'BWCA',
       'B365C>2.5', 'B365C<2.5', 'AHCh', 'B365CAHH', 'B365CAHA', 'home_rolling_goals_scored',
       'home_rolling_goals_conceded', 'home_rolling_shots_on_target',
       'home_rolling_corners', 'home_rolling_yellow_cards',
       'away_rolling_goals_scored', 'away_rolling_goals_conceded',
       'away_rolling_shots_on_target', 'away_rolling_corners',
       'away_rolling_yellow_cards']

scaler_vars = ['B365H', 'B365D', 'B365A', 'BWH', 'BWD', 'BWA', 'B365>2.5', 'B365<2.5',
       'AHh', 'B365CH', 'B365CD', 'B365CA', 'BWCH', 'BWCD', 'BWCA',
       'B365C>2.5', 'B365C<2.5', 'AHCh', 'B365CAHH', 'B365CAHA', 'Year',
       'Month', 'DayOfWeek', 'home_rolling_goals_scored',
       'home_rolling_goals_conceded', 'home_rolling_shots_on_target',
       'home_rolling_corners', 'home_rolling_yellow_cards',
       'away_rolling_goals_scored', 'away_rolling_goals_conceded',
       'away_rolling_shots_on_target', 'away_rolling_corners',
       'away_rolling_yellow_cards']

# =============================================================================
# TÍTULO PRINCIPAL
# =============================================================================
st.title('⚽ Predictor de Resultados - Premier League 2025/2026')
st.markdown("---")

# =============================================================================
# SECCIÓN 1: CALENDARIO DE PRÓXIMOS PARTIDOS
# =============================================================================
st.header("📅 Próximos partidos del calendario de la English Premier League")

# Creamos el DataFrame con los próximos partidos de la Jornada 31
proximos_partidos = pd.DataFrame({
    'Partido': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
    'Jornada': [31, 31, 31, 31, 31, 31, 31, 31],
    'Fecha': ['2026-03-20', '2026-03-21', '2026-03-21', '2026-03-21', '2026-03-21', '2026-03-22', '2026-03-22', '2026-03-22'],
    'Hora': ['20:00', '12:30', '15:00', '17:30', '20:00', '12:00', '14:15', '14:15'],
    'Local (HomeTeam)': ['Bournemouth', 'Brighton', 'Fulham', 'Everton', 'Leeds', 'Newcastle', 'Aston Villa', 'Tottenham'],
    'Visitante (AwayTeam)': ['Man United', 'Liverpool', 'Burnley', 'Chelsea', 'Brentford', 'Sunderland', 'West Ham', "Nott'm Forest"]
})

# Mostramos la tabla de partidos
st.dataframe(
    proximos_partidos,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# =============================================================================
# SECCIÓN 2: SELECTOR DE PARTIDO
# =============================================================================
st.header("🎯 Selecciona un Partido para Ver sus variables")

# Creamos las opciones del selector con formato descriptivo
opciones_partidos = []
for idx, row in proximos_partidos.iterrows():
    opcion = f"{row['Partido']} - {row['Local (HomeTeam)']} vs {row['Visitante (AwayTeam)']} ({row['Fecha']} {row['Hora']})"
    opciones_partidos.append(opcion)

# Selector de partido
partido_seleccionado = st.selectbox(
    "Elige el partido que deseas analizar:",
    options=opciones_partidos,
    index=0
)

# Extraemos el código del partido seleccionado (P1, P2, etc.)
codigo_partido = partido_seleccionado.split(" - ")[0]
indice_partido = int(codigo_partido[1]) - 1  # P1 -> índice 0, P2 -> índice 1, etc.

# Obtenemos los equipos del partido seleccionado
home_team = proximos_partidos.iloc[indice_partido]['Local (HomeTeam)']
away_team = proximos_partidos.iloc[indice_partido]['Visitante (AwayTeam)']

st.markdown("---")

# =============================================================================
# SECCIÓN 3: INFORMACIÓN DEL PARTIDO SELECCIONADO
# =============================================================================
st.header(f"📊 Información del Partido: {home_team} vs {away_team}")

# Buscamos los datos del partido en data_preparada
datos_partido = data_preparada[
    (data_preparada['HomeTeam'] == home_team) & 
    (data_preparada['AwayTeam'] == away_team)
]

if not datos_partido.empty:
    # Tomamos la primera coincidencia (el partido más reciente)
    partido_info = datos_partido.iloc[0]
    
    # Mostramos información básica del partido
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"🏠 Local: {home_team}")
        st.metric("Año", int(partido_info['Year']))
        st.metric("Mes", int(partido_info['Month']))
        st.metric("Día de la Semana", int(partido_info['DayOfWeek']))
    
    with col2:
        st.subheader(f"✈️ Visitante: {away_team}")
    
    st.markdown("---")
    
    # =============================================================================
    # CUOTAS DE APUESTAS
    # =============================================================================
    st.subheader("💰 Cuotas de Apuestas")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Bet365 - Resultado**")
        st.metric("Victoria Local (B365H)", f"{partido_info['B365H']:.2f}")
        st.metric("Empate (B365D)", f"{partido_info['B365D']:.2f}")
        st.metric("Victoria Visitante (B365A)", f"{partido_info['B365A']:.2f}")
    
    with col2:
        st.markdown("**Betway - Resultado**")
        st.metric("Victoria Local (BWH)", f"{partido_info['BWH']:.2f}")
        st.metric("Empate (BWD)", f"{partido_info['BWD']:.2f}")
        st.metric("Victoria Visitante (BWA)", f"{partido_info['BWA']:.2f}")
    
    with col3:
        st.markdown("**Goles Over/Under**")
        st.metric("Más de 2.5 goles", f"{partido_info['B365>2.5']:.2f}")
        st.metric("Menos de 2.5 goles", f"{partido_info['B365<2.5']:.2f}")
        st.metric("Asian Handicap (AHh)", f"{partido_info['AHh']:.2f}")
    
    st.markdown("---")
    
    # =============================================================================
    # CUOTAS DE CIERRE
    # =============================================================================
    st.subheader("📈 Cuotas de Cierre")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Bet365 Cierre**")
        st.metric("Victoria Local (B365CH)", f"{partido_info['B365CH']:.2f}")
        st.metric("Empate (B365CD)", f"{partido_info['B365CD']:.2f}")
        st.metric("Victoria Visitante (B365CA)", f"{partido_info['B365CA']:.2f}")
    
    with col2:
        st.markdown("**Betway Cierre**")
        st.metric("Victoria Local (BWCH)", f"{partido_info['BWCH']:.2f}")
        st.metric("Empate (BWCD)", f"{partido_info['BWCD']:.2f}")
        st.metric("Victoria Visitante (BWCA)", f"{partido_info['BWCA']:.2f}")
    
    with col3:
        st.markdown("**Goles y Asian Handicap Cierre**")
        st.metric("Más de 2.5 goles (C)", f"{partido_info['B365C>2.5']:.2f}")
        st.metric("Menos de 2.5 goles (C)", f"{partido_info['B365C<2.5']:.2f}")
        st.metric("Asian Handicap Cierre", f"{partido_info['AHCh']:.2f}")
    
    st.markdown("---")
    
    # =============================================================================
    # ESTADÍSTICAS ROLLING - EQUIPO LOCAL
    # =============================================================================
    st.subheader(f"📊 Estadísticas Recientes - {home_team} (Local) - Estos datos son un promedio de los últimos 8 partidos de local")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("⚽ Goles Anotados", f"{partido_info['home_rolling_goals_scored']:.2f}")
    with col2:
        st.metric("🥅 Goles Recibidos", f"{partido_info['home_rolling_goals_conceded']:.2f}")
    with col3:
        st.metric("🎯 Tiros a Puerta", f"{partido_info['home_rolling_shots_on_target']:.2f}")
    with col4:
        st.metric("🚩 Córners", f"{partido_info['home_rolling_corners']:.2f}")
    with col5:
        st.metric("🟨 Tarjetas Amarillas", f"{partido_info['home_rolling_yellow_cards']:.2f}")
    
    st.markdown("---")
    
    # =============================================================================
    # ESTADÍSTICAS ROLLING - EQUIPO VISITANTE
    # =============================================================================
    st.subheader(f"📊 Estadísticas Recientes - {away_team} (Visitante) - Estos datos son un promedio de los últimos 8 partidos de visitante")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("⚽ Goles Anotados", f"{partido_info['away_rolling_goals_scored']:.2f}")
    with col2:
        st.metric("🥅 Goles Recibidos", f"{partido_info['away_rolling_goals_conceded']:.2f}")
    with col3:
        st.metric("🎯 Tiros a Puerta", f"{partido_info['away_rolling_shots_on_target']:.2f}")
    with col4:
        st.metric("🚩 Córners", f"{partido_info['away_rolling_corners']:.2f}")
    with col5:
        st.metric("🟨 Tarjetas Amarillas", f"{partido_info['away_rolling_yellow_cards']:.2f}")

    st.markdown("---")
    
    # =============================================================================
    # SECCIÓN: PREDICCIÓN DEL MODELO
    # =============================================================================
    st.header("🔮 Predicción del Resultado")
    
    # Preparación de datos para predicción
    # 1. Crear copia de los datos del partido seleccionado
    datos_prediccion = datos_partido.copy()
    
    # 2. Convertir variables categóricas (HomeTeam, AwayTeam) a variables dummy
    datos_prediccion = pd.get_dummies(
        datos_prediccion, 
        columns=['HomeTeam', 'AwayTeam'], 
        drop_first=False, 
        dtype=int
    )
    
    # 3. Adicionar columnas faltantes que el modelo espera (equipos no presentes)
    datos_prediccion = datos_prediccion.reindex(columns=variables_1, fill_value=0)
    
    # 4. Normalizar variables numéricas con el scaler entrenado
    datos_prediccion[scaler_vars] = min_max_scaler_1.transform(datos_prediccion[scaler_vars])
    
    # 5. Realizar la predicción con el modelo
    Y_pred_encoded = model_1.predict(datos_prediccion)
    
    # 6. Decodificar la predicción según el criterio de entrenamiento
    # Mapeo: A=0 (Victoria Visitante), D=1 (Empate), H=2 (Victoria Local)
    mapeo_prediccion = {0: 'A', 1: 'D', 2: 'H'}
    Y_pred_label = mapeo_prediccion.get(Y_pred_encoded[0], 'Desconocido')
    
    # 7. Interpretar el resultado
    resultados_dict = {
        'H': {'texto': 'Victoria Local', 'emoji': '🏠', 'color': 'green', 'equipo': home_team},
        'D': {'texto': 'Empate', 'emoji': '🤝', 'color': 'orange', 'equipo': 'Ambos equipos'},
        'A': {'texto': 'Victoria Visitante', 'emoji': '✈️', 'color': 'blue', 'equipo': away_team}
    }
    
    resultado = resultados_dict.get(Y_pred_label, {'texto': 'Desconocido', 'emoji': '❓', 'color': 'gray', 'equipo': 'N/A'})
    
    # 8. Mostrar el resultado de forma visual
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        ">
            <h1 style="color: white; font-size: 3em; margin: 0;">{resultado['emoji']}</h1>
            <h2 style="color: white; margin: 10px 0;">{resultado['texto']}</h2>
            <p style="color: #ddd; font-size: 1.2em; margin: 5px 0;">
                <strong>{home_team}</strong> vs <strong>{away_team}</strong>
            </p>
            <p style="color: #aaa; font-size: 0.9em;">
                Predicción: <strong style="color: #ffd700;">{Y_pred_label}</strong> 
                (H=Local, D=Empate, A=Visitante)
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Mostrar información adicional sobre la predicción
    st.markdown("")
    with st.expander("📋 Ver detalles técnicos de la predicción"):
        st.markdown("**Proceso de predicción:**")
        st.markdown("""
        1. ✅ Datos del partido extraídos de `data_preparada.csv`
        2. ✅ Variables categóricas convertidas a dummy (One-Hot Encoding)
        3. ✅ Columnas faltantes añadidas con valor 0
        4. ✅ Variables numéricas normalizadas con MinMaxScaler
        5. ✅ Predicción realizada con el modelo entrenado
        """)
        
        st.markdown("**Criterio de decodificación:**")
        st.markdown("""
        | Código | Etiqueta | Significado |
        |--------|----------|-------------|
        | 0 | A | Victoria Visitante (Away) |
        | 1 | D | Empate (Draw) |
        | 2 | H | Victoria Local (Home) |
        """)
        
        st.markdown(f"**Resultado codificado:** `{Y_pred_encoded[0]}`")
        st.markdown(f"**Resultado decodificado:** `{Y_pred_label}`")
        st.markdown(f"**Interpretación:** {resultado['texto']}")

else:
    st.warning(f"⚠️ No se encontraron datos para el partido {home_team} vs {away_team} en el dataset.")
    st.info("Los datos del partido podrían no estar disponibles en nuestro servidor")

st.markdown("---")
st.caption("📌 Datos de la temporada 2020-2021 hasta 2025-2026 (Jornada 30) | Total: 1,820 partidos")
