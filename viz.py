
from general_functions import  plot, plot_candidates

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

y = pd.read_csv("y.csv", index_col=0)
x = pd.read_csv("x.csv",index_col=0)

y = y.reset_index()

st.write(plot(x))
st.write(plot_candidates(y))

st.write("©Simon Pastor")
st.write("Contact: simonjpastor@gmail.com")

st.info("Journaux de la Presse Quotidienne Régionale:Ouest-France, Sud Ouest, La Voix du Nord, Le Parisien, Le Télégramme, Le Dauphiné Libéré, Le Progrès, La Nouvelle République, La Montagne, Dernières Nouvelles d'Alsace, La Dépêche du Midi, L'Est Républicain, Le Républicain Lorrain, Midi Libre, Le Courrier de l'Ouest,  La Provence, L'Union - L'Ardennais, Nice Matin, L'Alsace, Le Courrier Picard, Le Journal de Saône-et-Loire, Var Matin, L'Indépendant, Paris Normandie, Le Maine Libre, Le Bien Public, Presse Océan, L'Yonne Républicaine, Nord Eclair, La Manche Libre, Ouest France Pays de La Loire, Ouest France Centre Val de Loire")
