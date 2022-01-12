from scrape_functions import scrape_parisnormandie,scrape_lamanchelibre,\
scrape_lavoixdunord, scrape_nordeclair, scrape_lunion, scrape_courrierpicard,\
scrape_estrepublicain, scrape_dna, scrape_lunion, scrape_lorrain, scrape_lalsace,\
scrape_lyonne, scrape_lejsl, scrape_bienpublic, scrape_leprogres, scrape_lamontagne,\
scrape_laprovence, scrape_nicematin, scrape_varmatin, scrape_midilibre, scrape_lindependant,\
scrape_leparisien, scrape_ladepeche, scrape_sudouest

from general_functions import progressBar, check_date, check_duplicates, tokenize, count_func, \
day_word, topic_count, topic_count2, stuff_topics, get_viz_df, plot, gen_driver, save_info, open_info

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import datetime
from datetime import date, datetime, timedelta
from selenium import webdriver
import chromedriver_binary
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import plotly.express as px
import squarify
import json
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go

# Presse Océane
presseoceane_titles = []; presseoceane_descriptions = []; presseoceane_dates = []
presseoceane = {"presseoceane_titles":presseoceane_titles, "presseoceane_descriptions":presseoceane_descriptions, "presseoceane_dates":presseoceane_dates}
for i,j in presseoceane.items():
    open_info(j,i)

#Ouest France Pays de la Loire
ouestfrancePL_titles = []; ouestfrancePL_descriptions = []; ouestfrancePL_dates= []
presseoceane = {"ouestfrancePL_titles":ouestfrancePL_titles, "ouestfrancePL_descriptions":ouestfrancePL_descriptions, "ouestfrancePL_dates":ouestfrancePL_dates}
for i,j in presseoceane.items():
    open_info(j,i)

#Ouest France Bretagne
ouestfranceBR_titles = []; ouestfranceBR_descriptions = []; ouestfranceBR_dates= []
presseoceane = {"ouestfranceBR_titles":ouestfranceBR_titles, "ouestfranceBR_descriptions":ouestfranceBR_descriptions, "ouestfranceBR_dates":ouestfranceBR_dates}
for i,j in presseoceane.items():
    open_info(j,i)

#Ouest Centre Val de Loire
ouestfranceCV_titles = []; ouestfranceCV_descriptions = []; ouestfranceCV_dates= []
presseoceane = {"ouestfranceCV_titles":ouestfranceCV_titles, "ouestfranceCV_descriptions":ouestfranceCV_descriptions, "ouestfranceCV_dates":ouestfranceCV_dates}
for i,j in presseoceane.items():
    open_info(j,i)

#Courrier de L'Ouest
courrierdelouest_titles = []; courrierdelouest_descriptions = []; courrierdelouest_dates= []
presseoceane = {"courrierdelouest_titles":courrierdelouest_titles, "courrierdelouest_descriptions":courrierdelouest_descriptions, "courrierdelouest_dates":courrierdelouest_dates}
for i,j in presseoceane.items():
    open_info(j,i)

#Le Maine Libre
lemainelibre_titles = []; lemainelibre_descriptions = []; lemainelibre_dates= []
presseoceane = {"lemainelibre_titles":lemainelibre_titles, "lemainelibre_descriptions":lemainelibre_descriptions, "lemainelibre_dates":lemainelibre_dates}
for i,j in presseoceane.items():
    open_info(j,i)

# Normandie
# parisnormandie_titles, parisnormandie_descriptions, parisnormandie_dates, driver, parisnormandie_keywords = scrape_parisnormandie()
# lamanchelibre_titles, lamanchelibre_descriptions, lamanchelibre_dates, driver = scrape_lamanchelibre()

# normandie_titles = parisnormandie_titles
# normandie_titles.extend(lamanchelibre_titles)
# normandie_descriptions = parisnormandie_descriptions
# normandie_descriptions.extend(lamanchelibre_descriptions)
# normandie_dates = parisnormandie_dates
# normandie_dates.extend(lamanchelibre_dates)

# no = {"normandie_titles":normandie_titles, "normandie_descriptions":normandie_descriptions, "normandie_dates":normandie_dates}
# for i,j in no.items():
#     save_info(j,i)

# Hauts de France
# lavoixdunord_titles, lavoixdunord_descriptions, lavoixdunord_dates,driver = scrape_lavoixdunord()
# nordeclair_titles, nordeclair_descriptions, nordeclair_dates = scrape_nordeclair()
#lunion_titles, lunion_descriptions, lunion_dates, driver, lunion_keywords = scrape_lunion()
# courrierpicard_titles,courrierpicard_descriptions, courrierpicard_dates = scrape_courrierpicard()

# nord_titles = lavoixdunord_titles
# nord_titles.extend(nordeclair_titles)
# nord_titles.extend(lunion_titles)
# nord_titles.extend(courrierpicard_titles)
# nord_descriptions = lavoixdunord_descriptions
# nord_descriptions.extend(nordeclair_descriptions)
# nord_descriptions.extend(lunion_descriptions)
# nord_descriptions.extend(courrierpicard_descriptions)
# nord_dates = lavoixdunord_dates
# nord_dates.extend(nordeclair_dates)
# nord_dates.extend(lunion_dates)
# nord_dates.extend(courrierpicard_dates)

# hdf = {"nord_titles":normandie_titles, "nord_descriptions":nord_descriptions, "nord_dates":nord_dates}
# for i,j in hdf.items():
#     save_info(j,i)

#Grand Est
# estrepublicain_titles, estrepublicain_descriptions, estrepublicain_dates,driver,estrepublicain_keywords = scrape_estrepublicain()
# dna_titles, dna_descriptions,dna_dates, driver, dna_keywords = scrape_dna(driver)
# lorrain_titles, lorrain_descriptions,lorrain_dates, driver, lorrain_keywords = scrape_lorrain()
# lalsace_titles, lalsace_descriptions,lalsace_dates, driver, lalsace_keywords = scrape_lalsace(driver)

# est_titles = estrepublicain_titles
# est_titles.extend(dna_titles)
# est_titles.extend(lunion_titles)
# est_titles.extend(lorrain_titles)
# est_titles.extend(lalsace_titles)
# est_descriptions = estrepublicain_descriptions
# est_descriptions.extend(dna_descriptions)
# est_descriptions.extend(lunion_descriptions)
# est_descriptions.extend(lorrain_descriptions)
# est_descriptions.extend(lalsace_descriptions)
# est_dates = estrepublicain_dates
# est_dates.extend(dna_dates)
# est_dates.extend(lunion_dates)
# est_dates.extend(lorrain_dates)
# est_dates.extend(lalsace_dates)

# est = {"est_titles":est_titles, "est_descriptions":est_descriptions, "est_dates":est_dates}
# for i,j in est.items():
#     save_info(j,i)

# #Bourgogne Franche Comté
# lyonne_titles, lyonne_descriptions, lyonne_dates, driver, lyonne_keywords = scrape_lyonne()
# lejsl_titles, lejsl_descriptions, lejsl_dates, driver, lejsl_keywords = scrape_lejsl(driver)
# bienpublic_titles, bienpublic_descriptions, bienpublic_dates, driver, bienpublic_keywords = scrape_bienpublic(driver)

# bourgogne_titles = lyonne_titles
# bourgogne_titles.extend(lejsl_titles)
# bourgogne_titles.extend(bienpublic_titles)
# bourgogne_descriptions = lyonne_descriptions
# bourgogne_descriptions.extend(lejsl_descriptions)
# bourgogne_descriptions.extend(bienpublic_descriptions)
# bourgogne_dates = lyonne_dates
# bourgogne_dates.extend(lyonne_dates)
# bourgogne_dates.extend(bienpublic_dates)

# bo = {"bourgogne_titles":bourgogne_titles, "bourgogne_descriptions":bourgogne_descriptions, "bourgogne_dates":bourgogne_dates}
# for i,j in bo.items():
#     save_info(j,i)

# #Auvergne
# leprogres_titles, leprogres_descriptions, leprogres_dates, driver = scrape_leprogres()
# lamontagne_titles, lamontagne_descriptions, lamontagne_dates, driver, lamontagne_keywords = scrape_lamontagne()

# auvergne_titles = leprogres_titles
# auvergne_titles.extend(lamontagne_titles)
# auvergne_descriptions = leprogres_descriptions
# auvergne_descriptions.extend(lamontagne_descriptions)
# auvergne_dates = leprogres_dates
# auvergne_dates.extend(lamontagne_dates)

# au = {"auvergne_titles":auvergne_titles, "auvergne_descriptions":auvergne_descriptions, "auvergne_dates":auvergne_dates}
# for i,j in au.items():
#     save_info(j,i)

# #PACA
# laprovence_titles, laprovence_descriptions,laprovence_dates, driver,laprovence_keywords = scrape_laprovence()
# nicematin_titles, nicematin_descriptions, nicematin_dates, driver = scrape_nicematin()
# varmatin_titles, varmatin_descriptions, varmatin_dates, driver = scrape_varmatin()

# paca_titles = nicematin_titles
# paca_titles.extend(laprovence_titles)
# paca_titles.extend(varmatin_titles)
# paca_descriptions = nicematin_descriptions
# paca_descriptions.extend(laprovence_descriptions)
# paca_descriptions.extend(varmatin_descriptions)
# paca_dates = nicematin_dates
# paca_dates.extend(laprovence_dates)
# paca_dates.extend(varmatin_dates)

# paca = {"paca_titles":paca_titles, "paca_descriptions":paca_descriptions, "paca_dates":paca_dates}
# for i,j in paca.items():
#     save_info(j,i)

# Occitanie
# midilibre_titles, midilibre_descriptions, midilibre_dates, driver = scrape_midilibre()
# lindependant_titles, lindependant_descriptions, lindependant_dates, driver = scrape_lindependant()

# occitanie_titles = midilibre_titles
# occitanie_titles.extend(lindependant_titles)
# occitanie_descriptions = midilibre_descriptions
# occitanie_descriptions.extend(lindependant_descriptions)
# occitanie_dates = midilibre_dates
# occitanie_dates.extend(lindependant_dates)

# oc = {"occitanie_titles":occitanie_titles, "occitanie_descriptions":occitanie_descriptions, "occitanie_dates":occitanie_dates}
# for i,j in oc.items():
#     save_info(j,i)

# Ile de France
# leparisien_titles, leparisien_descriptions, leparisien_dates, driver = scrape_leparisien()

# idf = {"leparisien_titles":leparisien_titles, "leparisien_descriptions":leparisien_descriptions, "leparisien_dates":leparisien_dates}
# for i,j in idf.items():
#     save_info(j,i)

# Nouvelle Aquitaine
# ladepeche_titles, ladepeche_descriptions, ladepeche_dates, driver = scrape_ladepeche()
# sudouest_titles, sudouest_descriptions, sudouest_dates, driver, sudouest_keywords= scrape_sudouest()

# aquitaine_titles = ladepeche_titles
# aquitaine_titles.extend(sudouest_titles)
# aquitaine_titles.extend(courrierdelouest_titles)
# #aquitaine_titles.extend(lanouvellerepublique_titles)
# aquitaine_descriptions = ladepeche_descriptions
# aquitaine_descriptions.extend(sudouest_descriptions)
# aquitaine_descriptions.extend(courrierdelouest_descriptions)
# #aquitaine_descriptions.extend(lanouvellerepublique_descriptions)
# aquitaine_dates = ladepeche_dates
# aquitaine_dates.extend(sudouest_dates)
# aquitaine_dates.extend(courrierdelouest_dates)
# #aquitaine_dates.extend(lanouvellerepublique_dates)

# aqui = {"aquitaine_titles":aquitaine_titles, "aquitaine_descriptions":aquitaine_descriptions, "aquitaine_dates":aquitaine_dates}
# for i,j in aqui.items():
#     save_info(j,i)

bretagne_titles = ouestfranceBR_titles
bretagne_descriptions = ouestfranceBR_titles
bretagne_dates = ouestfranceBR_dates

bretagne = {"bretagne_titles":bretagne_titles, "bretagne_descriptions":bretagne_descriptions, "bretagne_dates":bretagne_dates}
for i,j in bretagne.items():
    save_info(j,i)

loire_titles = presseoceane_titles
loire_titles.extend(ouestfrancePL_titles)
loire_titles.extend(courrierdelouest_titles)
loire_titles.extend(lemainelibre_titles)
loire_descriptions = presseoceane_descriptions
loire_descriptions.extend(ouestfrancePL_descriptions)
loire_descriptions.extend(courrierdelouest_descriptions)
loire_descriptions.extend(lemainelibre_descriptions)
loire_dates = presseoceane_dates
loire_dates.extend(ouestfrancePL_dates)
loire_dates.extend(courrierdelouest_dates)
loire_dates.extend(lemainelibre_dates)

loire = {"loire_titles":loire_titles, "loire_descriptions":loire_descriptions, "loire_dates":loire_dates}
for i,j in loire.items():
    save_info(j,i)

centre_titles = ouestfranceCV_titles
#centre_titles.extend(lanouvellerepublique_titles)
centre_descriptions = ouestfranceCV_descriptions
#centre_descriptions.extend(lanouvellerepublique_descriptions)
centre_dates = ouestfranceCV_dates
#centre_dates.extend(ouestfranceCV_dates)

centre = {"centre_titles":centre_titles, "centre_descriptions":centre_descriptions, "centre_dates":centre_dates}
for i,j in centre.items():
    save_info(j,i)
