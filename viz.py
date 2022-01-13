
from general_functions import  plot, plot_candidates, plot_all

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import datetime
from datetime import date, datetime, timedelta
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import json
import plotly.express as px
import streamlit as st



APP_NAME = "Analyse PQR"
st.markdown("<h1 style='text-align: center; color: black;'>Thèmes et Candidats mentionnés dans la Presse Quotidienne Régionale</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Semaine du 10 au 14 Janvier</h2>", unsafe_allow_html=True)

presse_nationale = pd.read_csv("presse_nationale.csv", index_col="Unnamed: 0")
y = pd.read_csv("y2.csv",index_col="Unnamed: 0").transpose()
y.insert(0,"",0)
y = pressenationale.join(y)
x = pd.read_csv("y.csv",index_col=0)


st.plotly_chart(plot_all(y), use_column_width=True)
st.plotly_chart(plot_candidates(x), use_column_width=True)

st.write("©Simon Pastor")
st.write("Contact: simonjpastor@gmail.com")
st.write("")

st.markdown("<h3 style='text-align: center; color: black;'><strong>Presse Quotidienne Régionale</strong></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center'>Ouest-France, Sud Ouest, La Voix du Nord, Le Parisien, Le Télégramme, Le Dauphiné Libéré, Le Progrès, La Nouvelle République, La Montagne, Dernières Nouvelles d'Alsace, La Dépêche du Midi, L'Est Républicain, Le Républicain Lorrain, Midi Libre, Le Courrier de l'Ouest,  La Provence, L'Union - L'Ardennais, Nice Matin, L'Alsace, Le Courrier Picard, Le Journal de Saône-et-Loire, Var Matin, L'Indépendant, Paris Normandie, Le Maine Libre, Le Bien Public, Presse Océan, L'Yonne Républicaine, Nord Eclair, La Manche Libre, Ouest France Pays de La Loire, Ouest France Centre Val de Loire</p>", unsafe_allow_html=True)
#st.write("Ouest-France, Sud Ouest, La Voix du Nord, Le Parisien, Le Télégramme, Le Dauphiné Libéré, Le Progrès, La Nouvelle République, La Montagne, Dernières Nouvelles d'Alsace, La Dépêche du Midi, L'Est Républicain, Le Républicain Lorrain, Midi Libre, Le Courrier de l'Ouest,  La Provence, L'Union - L'Ardennais, Nice Matin, L'Alsace, Le Courrier Picard, Le Journal de Saône-et-Loire, Var Matin, L'Indépendant, Paris Normandie, Le Maine Libre, Le Bien Public, Presse Océan, L'Yonne Républicaine, Nord Eclair, La Manche Libre, Ouest France Pays de La Loire, Ouest France Centre Val de Loire")

st.markdown("<h3 style='text-align: center; color: black;'><strong>Presse Nationale</strong></h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Le Monde, Le Figaro, Le Parisien, Les Echos, Le Point, Libération, Valeurs Actuelles</h3>", unsafe_allow_html=True)
