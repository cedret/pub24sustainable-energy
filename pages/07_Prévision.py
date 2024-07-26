#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:26:23 2024
05_Prévision.py
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
#from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score, mean_squared_error
#from sklearn.metrics import accuracy_score, confusion_matrix
#import statsmodels.api as sm
import plotly.graph_objects as go
import plotly.express as px

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

# ....... CORPS DE LA PAGE ......

df2 = st.session_state['df2']

st.header("Etude de l'accès aux énergies")
st.title('Prévisions')
st.write('Choix ou infos parfois dans la colonne de gauche, vers le bas')
st.write(f"Le dataframe actif contient {len(df2)} lignes")
st.write("Restriction vers df_fmr sur:")
#st.write("Objets exclus")
st.write("Aucun")
#st.write("Restriction de df_fmr à l'année 2000")

dfmr = df2.select_dtypes(exclude='object')

st.write(":red[En cas d'erreur, choisir des valeurs vides à supprimer sur le coté]")
df = st.session_state['df']
load_data= st.session_state['load_data']


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

supp_col = ['Country',
    'Renewables (% equivalent primary energy)',
    'Financial flows to developing countries (US $)',
    'Date',
    'Year',
    'Density (P/Km2)',
    'Land Area(Km2)',
    'Niveau population',
    'Sous-Continent'
    ]

# Supprimer les colonnes par leur nom
#df2fmr = df2.drop(columns=supp_col)

# Liste des colonnes objets à supprimer
df_num = df2.select_dtypes(exclude="object")

if st.sidebar.checkbox("Interpoler les valeurs manquantes"):
    df_num = df_num.interpolate()
st.sidebar.write((df_num.isna().sum().sum()),"valeurs manquantes dans le DataFrame")

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

if st.sidebar.checkbox("Afficher le dataframe résultant"):
    st.write(df_num)

# Déclaration de la target
cible="Electricity from renewables (TWh)"

Y = df_num[cible]

X = df_num.drop([cible], axis=1)  

### AUTRE CAS
# X = data1ref[['RevenuAnnuel','NbVisitesSite','PanierMoyen']] #Features
# Y = data1ref['DepensesAnnuelles'] #Target

st.write('Cible actuelle est:')
st.write(cible)

st.header('Prévisions par régression linéaire')

Xtrain, Xtest, Ytrain, Ytest = train_test_split (X, Y, test_size=0.2, random_state=42)

model2 = LinearRegression()

model2.fit(Xtrain, Ytrain)

Yfmr = model2.predict(Xtrain)
Ypred = model2.predict(Xtest)

comparaison = pd.DataFrame({'Valeurs réelles': Ytest, 'Valeurs prédites': Ypred.round(2)})
comparaison.reset_index(drop = True, inplace = True) #Reset de l'index

### Mesures de performance
#R2: Coefficient de détermination

#MSE: Erreur quadratique moyenne

mse = mean_squared_error (Ytest, Ypred)
r2 = r2_score (Ytest, Ypred)

st.write(f"Erreur quadratique moyenne= {mse}")
st.write(f"Coefficient de détermination R2= {r2}")

st.write(f"Intercept (constante) = {model2.intercept_}")
#coeff = pd.DataFrame(model1.coef_, ['Superficie','Chambres','AgeMaison','DistanceCentre','RevenuMoyenQuartier'])
coeff = pd.DataFrame(model2.coef_, X.columns)
#ajouter?? ,columns=['Coefficient']

if st.sidebar.checkbox("Afficher les coefficients"):
    st.write ("Les coefficients du modèle sont: ")
    st.write (coeff)

if st.sidebar.checkbox("Afficher une représentation graphique"):
    # Création du graphique avec Plotly
#    fig3 = px.scatter(df2, x='X', y='Y', title="Régression Linéaire")
#    fig3.add_trace(go.Scatter(x=Xtest, y=Ypred, mode='lines', name='Ligne de régression'))
    # Affichage du graphique avec Streamlit
#    st.plotly_chart(fig3)
 
    # Création du graphique avec Plotly
    fig4 = go.Figure()
    # Tracer les données d'entraînement
    fig4.add_trace(go.Scatter(x=Xtrain, y=Ytrain, mode='markers', name='Train Data', marker=dict(color='blue')))
    fig4.add_trace(go.Scatter(x=Xtrain, y=Yfmr, mode='lines', name='Train Fit', line=dict(color='blue')))
    # Tracer les données de test
    fig4.add_trace(go.Scatter(x=Xtest, y=Ytest, mode='markers', name='Test Data', marker=dict(color='red')))
    fig4.add_trace(go.Scatter(x=Xtest, y=Ypred, mode='lines', name='Test Fit', line=dict(color='red', dash='dot')))

    # Configuration du layout du graphique
    fig4.update_layout(
    title="Régression Linéaire - Données d'Entraînement et de Test",
    xaxis_title='X',
    yaxis_title='Y',
    legend_title='Légende',
    template='plotly_dark'
    )
    # Affichage du graphique avec Streamlit
    st.plotly_chart(fig4)    
    
st.sidebar.write("Compléments")
    
if st.sidebar.checkbox("Xtrain/ Ytrain"):
    st.write("Exemples de Xtrain", Xtrain.sample(5))
    st.write("Exemples de Ytrain", Ytrain.sample(5))
    
if st.sidebar.checkbox("Xtest/ Ytest"):
    st.write("Exemples de Xtest", Xtest.sample(5))
    st.write("Exemples de Ytest", Ytest.sample(5))

if st.sidebar.checkbox("Afficher quelques comparaisons"):
    st.write("Comparaison:", comparaison.sample(10))

if st.sidebar.checkbox("X en détails"):
    pfull(X)

#source1pred=[[20, 5, 100]]
#prediction = model2.predict(source1pred)
#st.write(f'Volume de vente estimé ={prediction[0].round(2)}')



