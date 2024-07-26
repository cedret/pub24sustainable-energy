#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:26:23 2024
01_Introduction.py
@author: access
"""

import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt


# ............ Chargement par défaut des données
#load_data = 'gdose30.csv'
#df = pd.read_csv(load_data)
#st.session_state['df']=df
df = st.session_state['df']

load_data= st.session_state['load_data']

df.rename(columns={'Unnamed: 0':'Inactif'}, inplace=True)
df['Inactif']=1

# ............ Présentation

st.title("Etude de l'accès aux énergies dans le monde")
st.header('Contexte')
st.write("Kaggle propose un [dataset](https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy) sur les consommations d'énergies de 175 pays entre 2000 et 2020.")
st.write("Il faut noter que les données sur la Russie ne sont pas présentes.")

st.header('Objectifs')
st.write("Comment répondre à l'objectif n°7 de l'[ONU](https://sdgs.un.org/fr/goals/goal7)?")

st.markdown(''' :orange[Garantir l’accès de tous à des services énergétiques fiables, durables et modernes, à un coût abordable]''')

#st.write(type(df_fmr))

df_fmr= df.copy()
df_fmr.columns = df.columns.str.lower()
df_fmr.columns = df_fmr.columns.astype('object')

fig2 = px.scatter_mapbox(
df,
lat="Latitude",
lon="Longitude",
hover_name="Country",
color="Population",
size_max=15,
zoom=3,
height=600,)
# Configuration de la carte
fig2.update_layout(
mapbox_style="carto-darkmatter",
margin={"r":0,"t":0,"l":0,"b":0}
)
# Affichage de la carte avec Streamlit
st.plotly_chart(fig2)

#st.map(df_fmr[['longitude','latitude']])

st.sidebar.write('Liste des indicateurs initiaux')
st.sidebar.write(df.columns)

#load_file = st.file_uploader('gdose30.csv conseillé')

# Vérification dataset
#if load_file is not None:
#    df = pd.read_csv(gdose30.csv)
#    st.session_state['df']=df