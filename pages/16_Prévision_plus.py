#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:26:23 2024
06_Prévision_Jose.py
@author: access
"""

import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

#from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score, mean_squared_error
#from sklearn.metrics import accuracy_score, confusion_matrix
#import statsmodels.api as sm

def pfull(truc):
    st.sidebar.write('.....P.F.U.L.L.....')
    st.sidebar.write(f'SHAPE: {(truc.shape)}')
    st.sidebar.write(f'LONGUEUR: {(len(truc))}')
#    st.sidebar.write('TYPE: {type(truc)}')
    st.sidebar.write(f'INDEX: {(truc.index)}')
    st.sidebar.write(f'VALUES: {(truc.values)}')
    # \n INFOS: {machin.info()}
    try:
        st.sidebar.write(f'COLONNES: {truc.columns}')
    except:
        st.sidebar.write ('Pas de colonnes')
    return

def evaluate_model(model):
    train_prev = model.predict(Xtrain)
    test_prev = model.predict(Xtest)
    rmse_train = mean_squared_error(Ytrain, train_prev, squared = False)
    rmse_test = mean_squared_error(Ytest, test_prev, squared = False)
    st.write(f"Rmse train={rmse_train}")
    st.write(f"Rmse test={rmse_test}")
    return

# ....... CORPS DE LA PAGE ......
st.title("Etude de l'accès aux énergies")

df = st.session_state['df']
load_data= st.session_state['load_data']
df2 = st.session_state['df2']

st.write(f"Le dataframe actif contient {len(df2)} lignes")

#'Access to electricity (% of population)': 'Accès électricité_%pop.',
#'Access to clean fuels for cooking': 'Cuisson avec hydroc.prop.',
#'Renewable-electricity-generating-capacity-per-capita': 'Elect. renouv/habit.',
#'Financial flows to developing countries (US $)': 'Flux finan. devel. pays_us$',
#'Renewable energy share in the total final energy consumption (%)': 'Part ener. renouv.',
#'Electricity from fossil fuels (TWh)': 'Source fossile_TWh',
#'Electricity from nuclear (TWh)': 'Source nucléaire_TWh',
#'Electricity from renewables (TWh)': 'Source renouvel_TWh',
#'Low-carbon electricity (% electricity)' :'Source bas carbone_%',
#'Primary energy consumption per capita (kWh/person)': 'Conso. ener. prim/habit_kWh/p',
#'Energy intensity level of primary energy (MJ/$2017 PPP GDP)': 'Intens. ener. prim_x',
#'Value_co2_emissions_kt_by_country': 'Emiss. CO2_kt/pays',
#'Renewables (% equivalent primary energy)': 'Renouv_%EPE',
#'Density (P/Km2)':'Densité_P/Km2',
#'Land Area(Km2)': 'Surface_Km2',

# Isolation des sources

# Liste des colonnes à supprimer
df_num = df2.select_dtypes(exclude="object")

if st.sidebar.checkbox("Supprimer colonnes avec valeurs manquantes"):
# Supprimer les colonnes contenant des valeurs manquantes
    df_num = df_num.dropna(axis=1)
    st.sidebar.write("lignes utiles", len(df_num))
        
if st.sidebar.checkbox("Supprimer lignes avec valeurs manquantes"):
# Supprimer les lignes contenant des valeurs manquantes
    df_num = df_num.dropna(axis=0)
    st.sidebar.write("lignes utiles", len(df_num))

if st.sidebar.checkbox("Afficher les variables"):
    st.write(df_num.columns)

if st.sidebar.checkbox("Afficher le dataframe entrant"):
    st.write(df_num)

# Features
X = df_num.drop("Renewable energy share (% of final consumption)", axis = 1)

# Target
Y = df_num["Renewable energy share (% of final consumption)"]

# Train/test split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size = 0.2, random_state=42)

st.write(Xtrain.shape, Ytrain.shape, Xtest.shape, Ytest.shape)

lr= LinearRegression()
lr.fit(Xtrain, Ytrain)

st.write("Linear regression:",evaluate_model(lr))

# modèle de foret aleatoire
rf = RandomForestRegressor(random_state=42)
rf.fit(Xtrain, Ytrain)

st.write("Random forest:",evaluate_model(rf))

st.sidebar.write("Prévisions depuis des données vierges.")
