#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:26:23 2024
03_Constats.py
@author: access
"""

import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

# ....... CORPS DE LA PAGE ......
df2 = st.session_state['df2']

st.header("Etude de l'accès aux énergies")
#st.write('Choix ou infos parfois dans la colonne de gauche, vers le bas')
st.sidebar.write(f"Le dataframe actif a pour format {df2.shape}")
#st.write("Restriction vers df_fmr sur:")
#st.write("Objets exclus")
#st.write("Aucun")
#st.write("Restriction de df_fmr à l'année 2000")

dfmr = df2.select_dtypes(exclude='object')
# ..... Page spécifique

st.title('Constats')

st.write("+ Russie absente.")

st.write("+ Année 2020 très incomplète, supprimée car ne dégrade pas l'étude.")

st.write("+ Beaucoup d'incertitudes sur les petits pays:")
st.write("++ Données incomplètes.")
st.write("++ Impact faible sur la population mondiale.")

st.markdown('---')  # Séparateur

st.write('Les valeurs manquantes avec un taux > 16%:')
st.write('+ Financial flows to developing countries (US $)')
st.write('+ Renewable electricity generating per capita')
st.write('+ Renewables (% equivalent primary energy)')

st.markdown('---')  # Séparateur

st.write('Les valeurs manquantes avec un taux < 9%:')
st.write('+ Value co2 emissions kt by country')
st.write('+ Electricity from nuclear (TWh)')
st.write('+ GDP per capita: Instable ou erroné ?')
st.write('+ GDP growth: Très instable ou erroné?')

st.markdown('---')  # Séparateur

st.write("Corrélations négatives liées à l'accès à l'électricité/ renouvelable")
st.write("Avec incidence sur les émissions de CO2, et polution?")
