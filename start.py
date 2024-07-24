#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:58:32 2024
str00test.py
@author: access
"""

import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

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

# Configurer la page pour une largeur maximale
st.set_page_config(layout="wide")

def intro():
    st.header('Introduction')
    st.write('Bienvenue')

def objecti():
    st.header('Objectifs')
    st.write('A préciser')

def stats(dataframe):
    st.header('Statistiques du dataset actuel')
    st.write(dataframe.describe())

def outils(dataframe):
    st.write('Avec support Youtube de Andy McDonald')
    st.write('+++ Comment afficher les apostrophes?')
    st.text('Affichage par st.text')
    
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=dataframe['Latitude'], y=dataframe['Longitude'])
    ax.set_xlabel('Latitude')
    ax.set_ylabel('Longitude')
    st.pyplot(fig)
    

def pratic(dataframe):
    # Créer un graphique en tarte Plotly
    fig = px.pie(dataframe, names='Sub_cont',
                 title='Sample Pie Chart')

    # Configurer l'application Streamlit
    st.title('Tarte Plotly')
    st.write('Graphique en tarte créé avec Plotly et intégré dans une application Streamlit.')

    # Afficher le graphique en tarte
    st.plotly_chart(fig)
    
def charger(dataframe):
    loaded_file = st.file_uploader('Charger votre csv')
    return loaded_file

def test(dataframe):
    st.title('Test Plotly express')
    x_axis_val=st.selectbox('Select X-Axis Value', options=df.columns)
    y_axis_val=st.selectbox('Select Y-Axis Value', options=df.columns)
    c_axis_val=st.selectbox('Select C-Axis Value', options=df.columns)
#    s_axis_val=st.selectbox('Select S-Axis Value', options=df.columns)
    
#    clr=st.color_picker('Choisir une couleur')
    plot = px.scatter(dataframe, x=x_axis_val, y=y_axis_val,
                      color=c_axis_val)
#    plot.update_traces(marker=dict(color=clr))
    st.plotly_chart(plot)

# ........... Début du corps du programme ...........

#charger(df)

st.title('Etude accès aux énergies dans le monde')
st.write('Juillet 2024')

img_nrj = Image.open('/home/access/Documents/datanalyst6_streamlit/pages/energy.jpg')
st.image(img_nrj, caption="Energie électrique, la plus moderne?", use_column_width=True)

load_data = 'gdose11.csv'

df = pd.read_csv(load_data)

st.session_state['df']=df
st.session_state['load_data']=load_data

#st.header('Charger un csv')

#load_file = st.file_uploader('gdose13.csv conseillé')

# Vérification dataset
#if load_file is not None:
#    df = pd.read_csv(load_file)
#    st.session_state['df']=df

