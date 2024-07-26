#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:26:23 2024
14_outil_pies.py
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
st.sidebar.write((df2.isna().sum().sum()),"valeurs manquantes dans le DataFrame")
#st.sidebar.write("Restriction vers df_fmr sur:")
#st.write("Objets exclus")
#st.sidebar.write("aucune")

############## spécifique #########

st.header('Graphiques des indicateurs dans le temps pour le critère sélectionné')
#st.header('A choisir dans la colonne de gauche.')

#st.write("Restriction de df_fmr à l'année 2000")
#df_fmr= df2.query('Year==2000')

if st.sidebar.checkbox("Exclure les variables objets"):
    df3 = df2.select_dtypes(exclude=['object'])
else:
    df3 = df2.copy()
    
# Sélectionner les colonnes à supprimer
colonnes_a_supprimer = st.sidebar.multiselect('Supprimez les graphiques inutiles:',
    options=df3.columns.tolist())

# Supprimer les colonnes sélectionnées
if colonnes_a_supprimer:
    df3 = df3.drop(columns=colonnes_a_supprimer)    

# Étape 2: Ajoutez un sélecteur pour choisir le nombre de colonnes
num_columns = st.sidebar.slider("Colonnes d'affichage':", min_value=1, max_value=4, value=2)

# Ajoutez un sélecteur pour afficher ou non les légendes
show_legend = st.sidebar.checkbox("Afficher les légendes", value=False)

# Création des colonnes dans Streamlit
#    num_columns = 3  # Nombre de colonnes par ligne
columns = st.columns(num_columns)

# Liste des catégories à afficher
categories = df3.columns

# Sélecteurs pour choisir les variables
#value_column = st.sidebar.selectbox('Select the numeric value', df3.columns, index=1)
name_column = st.sidebar.selectbox('Select the categorie value', df3.columns, index=0)
valeur=st.sidebar.selectbox('Choisir valeur', options=df3.columns)

# Création du graphique circulaire avec Plotly Express
#fig_pp = px.pie(df2, values=value_column, names=name_column,
#                 title=f'{name_column} Distribution by {value_column}', 
#                 labels={value_column: value_column}, hole=0.3)

for column in df3.columns:
        # Comptage des valeurs uniques dans la colonne
        value_counts = df3[column].value_counts().reset_index()
        value_counts.columns = [column, 'Count']
        
        # Création du pie chart avec Plotly Express
        fig_pp = px.pie(value_counts, values='Count', names=column, 
                     title=f'Distribution des valeurs dans la colonne {column}')
        
        # Affichage du pie chart
        fig.show()

# Affichage des pie charts pour chaque colonne
plot_pie_charts(df)


# Affichage des graphiques dans les colonnes
for i, category in enumerate(categories):
    with columns[i % num_columns]:

        fig_pp = px.pie(df3,
#                        values=value_column,
                        names=valeur,
#                 title=f'{name_column} Distribution by {value_column}',                         
                 title=f'{name_column} Distribution by {valeur}', 
#                 labels={value_column: value_column},
                 hole=0.3)

#        fig2 = px.line(data_frame = df2, x = 'Year', y= category
#                , color = "Country"
#                ,title=" v s " + str(var_x)
#                )
# Masquer ou afficher la légende en fonction de la sélection
        fig_pp.update_layout(showlegend=show_legend)
# Supprimer l'affichage du xlabel
        fig_pp.update_xaxes(title_text='')
        st.plotly_chart(fig_pp)
            
st.sidebar.write("Témoin pour légende")
fig3 = px.line(
                data_frame = df3, x = 'Year', y= "Inactif"
                , color = "Country"
#                ,title=" v s " + str(var_x)
                )
# Masquer ou afficher la légende en fonction de la sélection
fig3.update_layout(showlegend=True)
    # Supprimer l'affichage du ylabel
fig3.update_yaxes(title_text='')
    # Supprimer l'affichage des unités sur les axes x et y
fig3.update_xaxes(title_text='')
fig3.update_yaxes(title_text='')
st.sidebar.plotly_chart(fig3)

