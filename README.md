# ⚽ Premier League Match Predictor

<div align="center">

![Premier League](https://img.shields.io/badge/Premier%20League-2025%2F2026-purple?style=for-the-badge&logo=premierleague&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-green?style=for-the-badge&logo=scikit-learn&logoColor=white)

**Sistema de predicción de resultados de partidos de fútbol de la English Premier League utilizando técnicas de Machine Learning**

[🚀 Ver Aplicación en Vivo](https://despliegue-premiere-league-data.streamlit.app/) | [📊 Fuente de Datos](https://www.football-data.co.uk/englandm.php)

</div>

---

## 📋 Descripción del Proyecto

Este proyecto es una **práctica académica** desarrollada como parte de la asignatura de **Minería de Datos** en el programa de **Maestría en Ciencia de Datos** de la Universidad Pontificia Bolivariana (UPB).

El objetivo principal es construir y desplegar modelos de Machine Learning capaces de predecir:

1. **🎯 Resultado del partido**: Victoria Local (H), Empate (D) o Victoria Visitante (A)
2. **⚽ Gol del visitante**: Si el equipo visitante marcará al menos un gol (Sí/No)

La aplicación permite visualizar información detallada de los próximos partidos de la Premier League, incluyendo cuotas de apuestas y estadísticas históricas de rendimiento de los equipos.

---

## 👥 Autores

<table align="center">
  <tr>
    <td align="center">
      <strong>Julio Bertty</strong><br>
      <sub>Estudiante de Maestría en Ciencia de Datos</sub>
    </td>
    <td align="center">
      <strong>Leydy Osorio</strong><br>
      <sub>Estudiante de Maestría en Ciencia de Datos</sub>
    </td>
  </tr>
</table>

<p align="center">
  <strong>Universidad Pontificia Bolivariana (UPB)</strong><br>
  Maestría en Ciencia de Datos<br>
  Minería de Datos - 2026
</p>

---

## 📊 Fuente de Datos

Los datos utilizados en este proyecto fueron obtenidos de **[Football-Data.co.uk](https://www.football-data.co.uk/englandm.php)**, una fuente reconocida de datos históricos de fútbol europeo.

### Procesamiento de Datos

Se realizó una **depuración exhaustiva** de los datos originales que incluyó:

- ✅ Filtrado de temporadas desde **2020-2021 hasta 2025-2026** (Jornada 31)
- ✅ Selección de **casas de apuestas disponibles para Colombia** (Bet365, Betway)
- ✅ Eliminación de variables con datos faltantes o inconsistentes
- ✅ Cálculo de **estadísticas rolling** (promedio de últimos 8 partidos)
- ✅ Codificación de variables categóricas y normalización de variables numéricas

### Variables Utilizadas

| Categoría | Variables |
|-----------|-----------|
| **Equipos** | HomeTeam, AwayTeam |
| **Temporales** | Year, Month, DayOfWeek |
| **Cuotas Bet365** | B365H, B365D, B365A, B365CH, B365CD, B365CA |
| **Cuotas Betway** | BWH, BWD, BWA, BWCH, BWCD, BWCA |
| **Over/Under** | B365>2.5, B365<2.5, B365C>2.5, B365C<2.5 |
| **Asian Handicap** | AHh, AHCh, B365CAHH, B365CAHA |
| **Estadísticas Local** | home_rolling_goals_scored, home_rolling_goals_conceded, home_rolling_shots_on_target, home_rolling_corners, home_rolling_yellow_cards |
| **Estadísticas Visitante** | away_rolling_goals_scored, away_rolling_goals_conceded, away_rolling_shots_on_target, away_rolling_corners, away_rolling_yellow_cards |

**Total de partidos analizados:** 1,820+ partidos

---

## 🤖 Modelos de Machine Learning

### Modelo 1: Predicción de Resultado (FTR)

| Característica | Detalle |
|----------------|---------|
| **Algoritmo** | Regresión Logística |
| **Objetivo** | Predecir resultado: H (Local), D (Empate), A (Visitante) |
| **Preprocesamiento** | One-Hot Encoding + MinMaxScaler |
| **Codificación** | A=0, D=1, H=2 |

### Modelo 2: Predicción de Gol Visitante

| Característica | Detalle |
|----------------|---------|
| **Algoritmo** | Regresión Logística |
| **Objetivo** | Predecir si el visitante marca al menos 1 gol |
| **Codificación** | 0=No marca, 1=Sí marca |

---

## 🖥️ Tecnologías Utilizadas

<div align="center">

| Tecnología | Uso |
|------------|-----|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Lenguaje de programación |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) | Manipulación de datos |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) | Operaciones numéricas |
| ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) | Modelos de ML |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) | Interfaz web |
| ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) | Control de versiones |

</div>

---

## 📁 Estructura del Proyecto

```
despliegue_premiere_league_data/
│
├── app.py                  # Aplicación principal de Streamlit
├── modelLR_v1.pkl          # Modelo 1: Predicción de resultado (H/D/A)
├── modelLR_2_v1.pkl        # Modelo 2: Predicción de gol visitante
├── data_preparada.csv      # Dataset procesado para predicción
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto
```

---

## 🚀 Cómo Ejecutar Localmente

### Prerrequisitos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/jbcoolness/despliegue_premiere_league_data.git
cd despliegue_premiere_league_data
```

2. **Crear entorno virtual (opcional pero recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**
```bash
streamlit run app.py
```

5. **Abrir en el navegador**
```
http://localhost:8501
```

---

## 📱 Funcionalidades de la Aplicación

### 1. 📅 Calendario de Partidos
Visualización de los próximos partidos de la Premier League con fecha, hora y equipos.

### 2. 🎯 Selector de Partido
Selección interactiva del partido a analizar mediante un menú desplegable.

### 3. 💰 Cuotas de Apuestas
Visualización de cuotas de Bet365 y Betway para victoria local, empate y victoria visitante.

### 4. 📊 Estadísticas Rolling
Promedios de los últimos 8 partidos de cada equipo:
- Goles anotados y recibidos
- Tiros a puerta
- Córners
- Tarjetas amarillas

### 5. 🔮 Predicciones
- **Predicción 1**: Resultado del partido (H/D/A)
- **Predicción 2**: ¿El visitante marcará gol? (Sí/No)

---

## ⚠️ Aviso Importante

> **Disclaimer sobre la capacidad de predicción:**
>
> Estos modelos tienen una **capacidad moderada de predicción**. Sus resultados son mejores que una predicción aleatoria, pero deben interpretarse con **cautela**, ya que el fútbol es un fenómeno con **alta incertidumbre**.
>
> Los resultados mostrados son **estimaciones basadas en datos históricos y cuotas de apuestas**, no garantías de resultados reales. Este proyecto tiene fines exclusivamente **académicos y educativos**.

---

## 📄 Licencia

Este proyecto es de uso **académico y educativo**. Los datos utilizados son propiedad de [Football-Data.co.uk](https://www.football-data.co.uk/).

---

## 🙏 Agradecimientos

- **Universidad Pontificia Bolivariana (UPB)** - Por el programa de Maestría en Ciencia de Datos
- **Football-Data.co.uk** - Por proporcionar datos históricos de alta calidad
- **Streamlit** - Por la plataforma de despliegue gratuita

---

<div align="center">

**Desarrollado con ❤️ para la Maestría en Ciencia de Datos - UPB**

📅 Abril 2026

</div>
