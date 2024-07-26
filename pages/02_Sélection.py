#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:26:23 2024
02_Sélection.py
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
st.write("Cette page réduit le nombre de pays étudié aux 12 plus peuplés par défaut")
st.title('Pays par quantité de population')
st.write('Choix ou infos parfois dans la colonne de gauche, vers le bas')

df = st.session_state['df']
load_data= st.session_state['load_data']
st.sidebar.write("Données chargées par défaut:")
st.sidebar.write(load_data)

st.sidebar.write("Après sélection:")

list1pays = df.Country.unique()
list1popu = df.Population.unique()

#sum_array = np.sum(array)
tot1popu = np.sum(list1popu)
#tot1popu = df['Population'].sum()
#st.write(tot1popu, list1popu, type(list1popu))

st.write(f"{len(list1pays)} pays dans la liste initiale, représente {tot1popu/1000000:.2f}M d'habitants")
st.header('Sélection')

val_min = 0.05
val_max = float(100)

# Demander un nombre entier
#limi_popu = st.number_input("Entrez le seuil de population des pays retenus ?(en millions)", min_value=1, max_value=2000)
limi_popu = st.slider("Seuil de population des pays retenus (en millions)", min_value= val_max, max_value= val_min)

#st.dataframe(df.sample(5).T, use_container_width=True)

#limi_popu = 30000000

df2 = df[df['Population'] > limi_popu*1000000]

df_fmr = df2[["Country","Population"]]
df_fmr = df_fmr.drop_duplicates(subset=['Country'])
li2pays = df_fmr.Country.unique()
li2popu = df_fmr.Population.unique()

st.sidebar.write(f'La population cumulée des pays de plus de {limi_popu:.2f}M habitants est de  {df_fmr.Population.sum()/1000000:.2f}M')
tot2popu = df_fmr.sum()
#som_popu = df_fmr[df_fmr.Population > limi_popu].sum()

st.sidebar.write(f'Ces {len(li2pays)} pays contiennent presque {tot2popu.Population*100/tot1popu:.2f} pourcent de la population mondiale.')
        
# Calculer la population cumulée ......................
df_fmr['Cumul population'] = df_fmr['Population'].cumsum()

if st.sidebar.checkbox("Liste des pays sélectionnés"):
#    st.sidebar.write("Données de population :")
    st.sidebar.write(li2pays)

df2fmr= df2.copy()

# affichage monde
df2fmr.columns = df2fmr.columns.str.lower()
df2fmr.columns = df2fmr.columns.astype('object')
st.map(df2fmr[['longitude','latitude']])

# affichage des barres
st.bar_chart(df_fmr.set_index('Country')['Population'])
#st.line_chart(li2popu)

if st.sidebar.checkbox("Exclure les variables objets", value=True):
    df3 = df2.select_dtypes(exclude=['object'])
else:
    df3 = df2.copy()

st.sidebar.markdown('---')  # Séparateur

if st.sidebar.checkbox("Interpoler les valeurs manquantes"):
    df3 = df3.interpolate()
st.sidebar.write((df3.isna().sum().sum()),"valeurs manquantes dans le DataFrame")

if st.sidebar.checkbox("Affichage des statistiques descriptives"):
#    dfdes = df3.map('{:.2f}'.format)
    dfdes=df3.describe().T
    # Formatage des valeurs avec deux décimales
    dfdes = dfdes.applymap(lambda x: f'{x:.2f}')
    st.table(dfdes)

# Affichage des valeurs vides
if st.sidebar.checkbox("Liste des valeurs manquantes en %"):
    # Afficher les valeurs manquantes
    st.write("Valeurs manquantes du dataframe actuel")
    st.subheader('% de valeurs manquantes par colonne')
    st.write(detec_vv(df3))
    
if st.sidebar.checkbox("Afficher valeurs manquantes en %"):    
    affi_vv(detec_vv(df3))
    st.write("Tableau des valeurs manquantes")
    st.write(df3.isnull())

st.sidebar.markdown('---')  # Séparateur


if st.sidebar.checkbox("Box plotssss"):    
# Création des colonnes dans Streamlit
    num_columns = 2  # Nombre de colonnes par ligne
    columns = st.columns(num_columns)

# Liste des catégories à afficher
    categories = df3.columns

# Affichage des graphiques dans les colonnes
    for i, category in enumerate(categories):
        with columns[i % num_columns]:
            fig = px.box(df3, y=category, title=f'Box plot of {category}')
            st.plotly_chart(fig)

st.sidebar.write("pairplot")

if st.sidebar.checkbox("Partage dataframe réduit (ou rectifié)", value=True):
    st.session_state['df2']=df2
else:
    st.session_state['df2']=df3
