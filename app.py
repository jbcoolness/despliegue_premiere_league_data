# Cargamos librerías principales
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import streamlit as st

# Cargamos el modelo 1
with open('modelTree_v1.pkl', 'rb') as f:
    bundle = pickle.load(f)

model_1 = bundle['modelo']
variables_1 = bundle['features']
objetivo_1 = bundle['target_encoder']

# Cargamos el modelo 2
with open('modelTree_2_v1.pkl', 'rb') as f:
    bundle_2 = pickle.load(f)

model_2 = bundle_2['modelo']
variables_2 = bundle_2['features']
objetivo_2 = bundle_2['target_encoder']

# El data set se entreno con los datos desde la temporada 2020 - 2021 iniciada - 2020-09-12 hasta la temporada 2025 - 2026 (2026-03-16), exactamente en la Jornada 31 
#  Para un total de 1821 partidos



st.title('Modelo Para predecir el Resultado de un Partido de Futbol de la Actual Premier League')

Equipo_Local = st.selectbox('Equipo Local', ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Ipswich', 'Leeds', 'Leicester', 'Liverpool', 'Man City', 'Man United', 'Newcastle', 'Norwich', "Nott'm Forest", 'Sheffield United', 'Southampton', 'Sunderland', 'Tottenham', 'Watford', 'West Brom', 'West Ham', 'Wolves'])
Equipo_Visitante = st.selectbox('Equipo Visitante', ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Ipswich', 'Leeds', 'Leicester', 'Liverpool', 'Man City', 'Man United', 'Newcastle', 'Norwich', "Nott'm Forest", 'Sheffield United', 'Southampton', 'Sunderland', 'Tottenham', 'Watford', 'West Brom', 'West Ham', 'Wolves'])
Year = st.selectbox('Año', [2026])
Month = st.selectbox('Mes', [3, 4])

vars1 = ['Year', 'Month', 'DayOfWeek','HomeTeam', 'AwayTeam', 'B365H', 'B365D', 'B365A', 'BWH', 'BWD', 'BWA', 'B365>2.5', 'B365<2.5',
       'AHh', 'B365CH', 'B365CD', 'B365CA', 'BWCH', 'BWCD', 'BWCA',
       'B365C>2.5', 'B365C<2.5', 'AHCh', 'B365CAHH', 'B365CAHA', 'home_rolling_goals_scored',
       'home_rolling_goals_conceded', 'home_rolling_shots_on_target',
       'home_rolling_corners', 'home_rolling_yellow_cards',
       'away_rolling_goals_scored', 'away_rolling_goals_conceded',
       'away_rolling_shots_on_target', 'away_rolling_corners',
       'away_rolling_yellow_cards']
