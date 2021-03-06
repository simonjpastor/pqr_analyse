
from general_functions import  plot, plot_candidates, plot_all, plot_national

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

# Latest Week
st.markdown("<h2 style='text-align: center; color: black;'>Période du 11 Février au 18 Février</h2>", unsafe_allow_html=True)
presse_nationale = pd.read_csv("presse_nationale5.csv", index_col="Unnamed: 0")
y = pd.read_csv("y6.csv",index_col="Unnamed: 0").transpose()
y.insert(0,"",0)
y = presse_nationale.join(y)
x = pd.read_csv("x6.csv",index_col=0)
candidats_pn = pd.read_csv("candidats_presse_nationale6.csv",index_col=0)
st.write(plot_all(y),use_column_width=True)

st.plotly_chart(plot_candidates(x), use_column_width=True)
st.plotly_chart(plot_national(candidats_pn), use_column_width=True)

# Latest Week
st.markdown("<h2 style='text-align: center; color: black;'>Période du 28 Janvier au 3 Février</h2>", unsafe_allow_html=True)
presse_nationale = pd.read_csv("presse_nationale4.csv", index_col="Unnamed: 0")
y = pd.read_csv("y5.csv",index_col="Unnamed: 0").transpose()
y.insert(0,"",0)
y = presse_nationale.join(y)
x = pd.read_csv("x5.csv",index_col=0)
candidats_pn = pd.read_csv("candidats_presse_nationale5.csv",index_col=0)
st.write(plot_all(y),use_column_width=True)

st.plotly_chart(plot_candidates(x), use_column_width=True)
st.plotly_chart(plot_national(candidats_pn), use_column_width=True)

# Latest Week
st.markdown("<h2 style='text-align: center; color: black;'>Période du 21 au 27 Janvier</h2>", unsafe_allow_html=True)
presse_nationale = pd.read_csv("presse_nationale3.csv", index_col="Unnamed: 0")
y = pd.read_csv("y4.csv",index_col="Unnamed: 0").transpose()
y.insert(0,"",0)
y = presse_nationale.join(y)
x = pd.read_csv("x4.csv",index_col=0)
candidats_pn = pd.read_csv("candidats_presse_nationale4.csv",index_col=0)
st.write(plot_all(y),use_column_width=True)

st.plotly_chart(plot_candidates(x), use_column_width=True)
st.plotly_chart(plot_national(candidats_pn), use_column_width=True)


# Latest Week
st.markdown("<h2 style='text-align: center; color: black;'>Période du 14 au 20 Janvier</h2>", unsafe_allow_html=True)
presse_nationale = pd.read_csv("presse_nationale2.csv", index_col="Unnamed: 0")
y = pd.read_csv("y3.csv",index_col="Unnamed: 0").transpose()
y.insert(0,"",0)
y = presse_nationale.join(y)
x = pd.read_csv("x3.csv",index_col=0)
candidats_pn = pd.read_csv("candidats_presse_nationale2.csv",index_col=0)
st.write(plot_all(y),use_column_width=True)

st.plotly_chart(plot_candidates(x), use_column_width=True)
st.plotly_chart(plot_national(candidats_pn), use_column_width=True)

# Week Prior
st.markdown("<h2 style='text-align: center; color: black;'>Période du 7 au 13 Janvier</h2>", unsafe_allow_html=True)
presse_nationale = pd.read_csv("presse_nationale.csv", index_col="Unnamed: 0")
y = pd.read_csv("y2.csv",index_col="Unnamed: 0").transpose()
y.insert(0,"",0)
y = presse_nationale.join(y)
x = pd.read_csv("y.csv",index_col=0)
candidats_pn = pd.read_csv("candidats_presse_nationale.csv",index_col=0)
st.write(plot_all(y),use_column_width=True)

st.plotly_chart(plot_candidates(x), use_column_width=True)
st.plotly_chart(plot_national(candidats_pn), use_column_width=True)

st.write("©Simon Pastor")
st.write("Contact: simonjpastor@gmail.com")
st.write("")

st.markdown("<h3 style='text-align: center; color: black;'><strong>Presse Quotidienne Régionale</strong></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center'>Ouest-France, Sud Ouest, La Voix du Nord, Le Parisien, Le Télégramme, Le Dauphiné Libéré, Le Progrès, La Nouvelle République, La Montagne, Dernières Nouvelles d'Alsace, La Dépêche du Midi, L'Est Républicain, Le Républicain Lorrain, Midi Libre, Le Courrier de l'Ouest,  La Provence, L'Union - L'Ardennais, Nice Matin, L'Alsace, Le Courrier Picard, Le Journal de Saône-et-Loire, Var Matin, L'Indépendant, Paris Normandie, Le Maine Libre, Le Bien Public, Presse Océan, L'Yonne Républicaine, Nord Eclair, La Manche Libre, Ouest France Pays de La Loire, Ouest France Centre Val de Loire</p>", unsafe_allow_html=True)
#st.write("Ouest-France, Sud Ouest, La Voix du Nord, Le Parisien, Le Télégramme, Le Dauphiné Libéré, Le Progrès, La Nouvelle République, La Montagne, Dernières Nouvelles d'Alsace, La Dépêche du Midi, L'Est Républicain, Le Républicain Lorrain, Midi Libre, Le Courrier de l'Ouest,  La Provence, L'Union - L'Ardennais, Nice Matin, L'Alsace, Le Courrier Picard, Le Journal de Saône-et-Loire, Var Matin, L'Indépendant, Paris Normandie, Le Maine Libre, Le Bien Public, Presse Océan, L'Yonne Républicaine, Nord Eclair, La Manche Libre, Ouest France Pays de La Loire, Ouest France Centre Val de Loire")

st.markdown("<h3 style='text-align: center; color: black;'><strong>Presse Nationale</strong></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Le Monde, Le Figaro, Le Parisien, Les Echos, Le Point, Libération, Valeurs Actuelles</p>", unsafe_allow_html=True)
