#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 16:53:29 2024
16_heatmap.py
@author: access
"""
import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configurer la page pour une largeur maximale
st.set_page_config(layout="wide")

df = st.session_state['df']
df2 = st.session_state['df2']
df3 = st.session_state['df2']

st.header("Etude de l'accès aux énergies")
st.title("Visuels ciblés")
st.write('Choix ou infos parfois dans la colonne de gauche, vers le bas')
st.sidebar.write(f"Le dataframe actif contient {df2.shape}")
st.sidebar.write((df2.isna().sum().sum()),"valeurs manquantes dans le DataFrame")

if st.sidebar.checkbox("Exclure les variables objets", value=True):
    df3 = df2.select_dtypes(exclude=['object'])
else:
    df3 = df2.copy()

if st.sidebar.checkbox("Interpoler les valeurs manquantes"):
    df3 = df3.interpolate()

# Titre de l'application
#df2 = df2.select_dtypes(include=['int64', 'float64'])
#df3 = df3.select_dtypes(include=['int64', 'float64'])

# Sélectionner les colonnes à supprimer
colonnes_a_supprimer = st.sidebar.multiselect(
    'Sélectionnez les colonnes à supprimer :',
    options=df3.columns.tolist()
)

# Supprimer les colonnes sélectionnées
if colonnes_a_supprimer:
    df3 = df3.drop(columns=colonnes_a_supprimer)

# Isolation des sources
X = df.drop([
#    'Unnamed: 0',
#    'Country',
    'Electricity from renewables (TWh)',
    'Financial flows to developing countries (US $)',
#    'Date',
    'Year',
    'Density (P/Km2)',
    'Land Area(Km2)',
#    'Niveau population',
#    'Sous-Continent'
    ], axis=1)

#correlation = df2.corr()
correlation = df3.corr()

# Configurer le style de Matplotlib pour un fond noir
plt.style.use('dark_background')

st.sidebar.markdown('---')  # Séparateur

if st.sidebar.checkbox("Afficher la heatmap", value=True):
    st.title('Heatmap ajustable')
# Créer la heatmap avec seaborn
    fig, ax = plt.subplots()
#sns.heatmap(data, ax=ax, cmap = "viridis")
#sns.heatmap(correlation, ax=ax)
    sns.heatmap(correlation, ax = ax, annot=False, cmap = "viridis", fmt=".2f", square=True)
#plt.xticks(rotation=60)
# Afficher la heatmap dans Streamlit
    st.pyplot(fig)

if st.sidebar.checkbox("Afficher la matrice de correlation"):
    st.table(correlation)

st.sidebar.markdown('---')  # Séparateur

if st.sidebar.checkbox("Plotly histogramme ajustable"):
    col_num = df2.select_dtypes(exclude='object').columns.to_list()
    var_x = st.selectbox("Histogramme variable X", col_num)
    var_y = st.selectbox("Histogramme variable Y", col_num)

    col_obj = df2.select_dtypes(include='object').columns.to_list()
    var_col = st.selectbox("Variable en couleur", col_obj)
#    fig1 = px.bar(data_frame = df2, x="Niveau population",
#        y="Electricity from nuclear (TWh)", title="Nuclear")
    fig1 = px.histogram(
        data_frame=df2, x = var_x, y= var_y, color = var_col,
        title=str(var_y) + " v s " + str(var_x))
    st.plotly_chart(fig1)

if st.sidebar.checkbox("Plotly scatter ajustable"):
    col_num = df2.select_dtypes(exclude='object').columns.to_list()
    var_x = st.selectbox("Variable en X", col_num)
    var_y = st.selectbox("Variable en Y", col_num)

    col_obj = df2.select_dtypes(include='object').columns.to_list()
    var_col = st.selectbox("Variable en couleur", col_obj)

    fig2 = px.scatter(
        data_frame=df2, x = var_x, y= var_y, color = var_col,
        title=str(var_y) + " v s " + str(var_x)
    )
    st.plotly_chart(fig2)

st.sidebar.markdown('---')  # Séparateur
df5=df2.copy()

if st.sidebar.checkbox("Tarte valeur simple"):
    valeur=st.sidebar.selectbox('Choisir valeur', options=df5.columns)
    fig = px.pie(df5, names=valeur, title=valeur)
    # Afficher le graphique
    st.plotly_chart(fig)

if st.sidebar.checkbox("Tarte valeur double"):
# Sélecteurs pour choisir les variables
    value_column = st.sidebar.selectbox('Select the numeric value', df5.columns, index=1)
    name_column = st.sidebar.selectbox('Select the categorie value', df5.columns, index=0)
# Création du graphique circulaire avec Plotly Express
    fig_pp = px.pie(df5, values=value_column, names=name_column,
                 title=f'{name_column} Distribution by {value_column}', 
                 labels={value_column: value_column}, hole=0.3)
# Affichage du graphique dans Streamlit
    st.plotly_chart(fig_pp)
    
st.sidebar.markdown('---')  # Séparateur