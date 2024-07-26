#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:26:23 2024
10_xxxxx Recherches xxxxx.py
@author: access
"""

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

# ....... CORPS DE LA PAGE ......
df2 = st.session_state['df2']

st.header("Etude de l'accès aux énergies")

st.write('Choix ou infos parfois dans la colonne de gauche, vers le bas')
st.write(f"Le dataframe actif contient {len(df2)} lignes")
st.write("Restriction vers df_fmr sur:")
st.write("Objets exclus")
#st.write("Restriction de df_fmr à l'année 2000")

df2 = st.session_state['df2']

dfmr = df2.select_dtypes(exclude='object')

st.title('Outils externes pour tests')


df2 = df2.select_dtypes(exclude='object')

st.write("Restriction de df_fmr à l'année 2000")
df_fmr= df2.query('Year==2000')

#pfull(df_fmr)

if st.sidebar.checkbox("plt.plot/scatter(avec x,y symétriques)"):
    val_x = 'Access to electricity (% of population)'
    val_y = 'Access to clean fuels for cooking'
    fig_pp, ax = plt.subplots()
    ax.scatter(df_fmr[val_x], df_fmr[val_y])
    ax.set_xlabel(val_x)
    ax.set_ylabel(val_y)
    ax.set_title("Plot de y selon x")
    st.pyplot(fig_pp)

if st.sidebar.checkbox("sns.histplot"):
    fig_sb, ax_sb = plt.subplots()
    ax_sb = sns.histplot(df_fmr["Population"])
    plt.xlabel("Population")
    st.pyplot(fig_sb)

if st.sidebar.checkbox("plt.hist"):
    fig_mt, ax_mt = plt.subplots()
    ax_mt = plt.hist(df_fmr["Population"])
    plt.xlabel("Population")
    st.pyplot(fig_mt)

if st.sidebar.checkbox("sns.pairplot(df2)"):
    fig_sb_pp = sns.pairplot(df2)
    st.pyplot(fig_sb_pp)

if st.sidebar.checkbox("Matrice (KO?): plotting.scatter"):
    pd.plotting.scatter_matrix(df2, figsize=(6,6),diagonal = 'kde',color="orange");
