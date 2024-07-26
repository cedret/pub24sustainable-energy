#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:26:23 2024
13_outil_bars.py
@author: access
"""

import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def pfull(truc):
    st.sidebar.write('.....P.F.U.L.L.....')
    st.sidebar.write(f'SHAPE: {(truc.shape)}')
    st.sidebar.write(f'LONGUEUR: {(len(truc))}')
    st.sidebar.write(f'TYPE: {type(truc)}')
    st.sidebar.write(f'INDEX: {(truc.index)}')
    st.sidebar.write(f'VALUES: {(truc.values)}')
    # \n INFOS: {machin.info()}
    try:
        st.sidebar.write(f'COLONNES: {truc.columns}')
    except:
        st.sidebar.write ('Pas de colonnes')
    return

# ....... CORPS DE LA PAGE ......
df2 = st.session_state['df2']

st.header("Etude de l'accès aux énergies")

st.write('Choix ou infos parfois dans la colonne de gauche, vers le bas')
st.sidebar.write(f"Le dataframe actif est {df2.shape}")
#st.sidebar.write((df2.isna().sum().sum()),"valeurs manquantes dans le DataFrame")
#st.sidebar.write("Restriction vers df_fmr sur:")
#st.write("Objets exclus")
#st.sidebar.write("aucune")

#dfmr = df2.select_dtypes(exclude='object')
############## spécifique #########

st.header('Graphiques des indicateurs dans le temps pour les pays sélectionnés')
#st.header('A choisir dans la colonne de gauche.')

#st.write("Restriction de df_fmr à l'année 2000")
#df_fmr= df2.query('Year==2000')

#if st.sidebar.checkbox("Exclure les variables objets"):
#    df3 = df2.select_dtypes(exclude=['object'])
#else:

df3 = df2.copy()
# Sélectionner les colonnes à supprimer
colonnes_a_supprimer = st.sidebar.multiselect(
    'Sélectionnez les graphiques inutiles :',
    options=df3.columns.tolist()
    )

# Supprimer les colonnes sélectionnées
if colonnes_a_supprimer:
    df3 = df3.drop(columns=colonnes_a_supprimer)    

# Choix de la colonne à utiliser pour les couleurs
col_col = st.sidebar.selectbox('Choisissez une colonne pour la couleur:', df3.columns)

# Création du slider pour choisir l'année
#choix = st.sidebar.slider('Choisissez une année', min_value=2000, max_value=2019) 
#                          value=int(df['Année'].min()))
#                              value=int(df['Year'].min()))
#df4 = df3.copy()
#Test moyenne par an
if st.sidebar.checkbox("test"):
    df4 = df3.groupby('Year').mean().reset_index()
else:
    choix = st.sidebar.slider('Choisissez une année', min_value=2000, max_value=2019) 
    df4 = df3[df3['Year'] == choix]

#st.write(choix, type(choix))
#types_colonne1 = df3['Year'].apply(type)
#st.write(types_colonne1)

# Filtrage des données pour l'année sélectionnée

if st.sidebar.checkbox("Interpoler les valeurs manquantes"):
    df4 = df4.interpolate()
st.sidebar.write((df4.isna().sum().sum()),"valeurs manquantes dans le DataFrame")


# Étape 2: Ajoutez un sélecteur pour choisir le nombre de colonnes
num_columns = st.sidebar.slider("Select number of columns:", min_value=1, max_value=4, value=2)
    
# Ajoutez un sélecteur pour afficher ou non les légendes
#show_legend = st.sidebar.checkbox("Afficher les légendes", value=False)

# Création des colonnes dans Streamlit
#    num_columns = 3  # Nombre de colonnes par ligne
columns = st.columns(num_columns)

# Liste des catégories à afficher
categories = df3.columns

# Affichage des graphiques dans les colonnes
for i, category in enumerate(categories):
    with columns[i % num_columns]:
#            fig = px.box(dfmr, y=category, title=f'Box plot of {category}')

        px2br = px.bar(df4, x='Country', y=category,
                       color=col_col,
#                       color_continuous_scale='bluered',
                       template='plotly_dark')

#        fig2 = px.line(data_frame = df2, x = 'Year', y= category
#                , color = "Country"
#                ,title=" v s " + str(var_x)                )

# Masquer ou afficher la légende en fonction de la sélection
        px2br.update_layout(showlegend=True)
# Supprimer l'affichage du xlabel
        px2br.update_xaxes(title_text='')
        st.plotly_chart(px2br)
