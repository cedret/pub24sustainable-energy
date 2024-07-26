#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:26:23 2024
14_Bilan.py
@author: access
"""
import numpy as np
import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# FONCTION POUR EXTRAIRE LE % DE VALEURS VIDES D'UN DATAFRAME
def detec_vv(df_fmr):
    # Calcul des valeurs manquantes
    list_vv = df_fmr.isnull().sum()
    perc_vv = (df_fmr.isnull().mean() * 100).round(2)
    tri_vv = perc_vv.sort_values(ascending=False)
#    pfull(tri_vv)
#    tri_vv = sorted(perc_vv, reverse=True)
#    st.write(type(list_vv))
# Affiche le nombre de valeurs manquantes pour chaque colonne
    return(tri_vv)

def affi_vv(vv):
    st.subheader('Bargraph des valeurs manquantes en %')
    # Slider pour ajuster la largeur du bargraph
#    width = st.slider("Adjust the width of the bargraph", min_value=5, max_value=25, value=12)

    #Bargraph des pourcentages de valeurs manquantes
#    fig, ax = plt.subplots(figsize=(width, 6))  # Utiliser la valeur du slider pour la largeur
    fig, ax = plt.subplots()
#   figsize=(15,10)
    vv.plot(kind='bar', ax=ax)
    ax.set_ylabel('% Valeurs manquantes')
#    plt.xticks(rotation=60)
    st.pyplot(fig)
    
#    percent_vid = data_ref.isna().sum() /data_ref.shape[0] *100
#    print ('_____CALC_VID_____', type(percent_vid), percent_vid.shape, percent_vid.info)
    return

st.header("Etude de l'accès aux énergies")

st.title("Méthode")

st.header("1 Traitements avec jupyter Notebook")

st.write("Premières visualisations")
st.write("Détections des anomalies")
st.write("Rectification d'anomalies")
st.write("Ajouts d'indicateurs: Population, sous-continents")
st.write("Réagencement des colonnes")
st.write("Génération d'un dataframe de travail")

st.header("2 Visualisation avec Streamlit")
st.write("Création de la structure")
st.write("Création des grilles de graphiques")
st.write("Création des outils d'affinage: Gestion ddes valeurs manquantes")

st.header("3 Finalisation d'un dashboard avec Streamlit")
st.write("Etape suivante")
st.write("Test de machine learning avancés")

if st.sidebar.checkbox("Afficher test"):
    st.write('***Plotly_chart(fig=px.scatter)***')
    fig2 = px.scatter(
        data_frame = df, x = 'Year', y= 'Electricity from renewables (TWh)', color = 'Niveau population',
        #title=" v s " + str(var_x)
        )
    st.plotly_chart(fig2)
