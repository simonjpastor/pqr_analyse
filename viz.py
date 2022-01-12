from scrape_functions import scrape_parisnormandie,scrape_lamanchelibre,\
scrape_lavoixdunord, scrape_nordeclair, scrape_lunion, scrape_courrierpicard,\
scrape_estrepublicain, scrape_dna, scrape_lunion, scrape_lorrain, scrape_lalsace,\
scrape_lyonne, scrape_lejsl, scrape_bienpublic, scrape_leprogres, scrape_lamontagne,\
scrape_laprovence, scrape_nicematin, scrape_varmatin, scrape_midilibre, scrape_lindependant,\
scrape_leparisien, scrape_ladepeche, scrape_sudouest

from general_functions import progressBar, check_date, check_duplicates, tokenize, count_func, \
day_word, topic_count, topic_count2, stuff_topics, get_viz_df, plot, gen_driver, save_info, open_info,\
stuff_candidates, get_viz_candidates, plot_candidates

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
import streamlit as s



normandie_titles = []; normandie_descriptions = []; normandie_dates= []
normandie = {"normandie_titles":normandie_titles, "normandie_descriptions":normandie_descriptions, "normandie_dates":normandie_dates}
for i,j in normandie.items():
    open_info(j,i)

nord_titles = []; nord_descriptions = []; nord_dates= []
nord = {"nord_titles":nord_titles, "nord_descriptions":nord_descriptions, "nord_dates":nord_dates}
for i,j in nord.items():
    open_info(j,i)

est_titles = []; est_descriptions = []; est_dates= []
est = {"est_titles":nord_titles, "est_descriptions":est_descriptions, "est_dates":est_dates}
for i,j in est.items():
    open_info(j,i)

bourgogne_titles = []; bourgogne_descriptions = []; bourgogne_dates= []
bourgogne = {"est_titles":bourgogne_titles, "bourgogne_descriptions":bourgogne_descriptions, "bourgogne_dates":bourgogne_dates}
for i,j in bourgogne.items():
    open_info(j,i)

auvergne_titles = []; auvergne_descriptions = []; auvergne_dates= []
auvergne= {"auvergne_titles":auvergne_titles, "auvergne_descriptions":auvergne_descriptions, "auvergne_dates":auvergne_dates}
for i,j in auvergne.items():
    open_info(j,i)

paca_titles = []; paca_descriptions = []; paca_dates= []
paca= {"paca_titles":paca_titles, "paca_descriptions":paca_descriptions, "paca_dates":paca_dates}
for i,j in paca.items():
    open_info(j,i)

occitanie_titles = []; occitanie_descriptions = []; occitanie_dates= []
occitanie= {"occitanie_titles":occitanie_titles, "occitanie_descriptions":occitanie_descriptions, "occitanie_dates":occitanie_dates}
for i,j in occitanie.items():
    open_info(j,i)

leparisien_titles = []; leparisien_descriptions = []; leparisien_dates= []
leparisien= {"leparisien_titles":leparisien_titles, "leparisien_descriptions":leparisien_descriptions, "leparisien_dates":leparisien_dates}
for i,j in leparisien.items():
    open_info(j,i)

aquitaine_titles = []; aquitaine_descriptions = []; aquitaine_dates= []
aquitaine= {"aquitaine_titles":aquitaine_titles, "aquitaine_descriptions":aquitaine_descriptions, "aquitaine_dates":aquitaine_dates}
for i,j in aquitaine.items():
    open_info(j,i)

loire_titles = []; loire_descriptions = []; loire_dates= []
loire= {"loire_titles":loire_titles, "loire_descriptions":loire_descriptions, "loire_dates":loire_dates}
for i,j in loire.items():
    open_info(j,i)

bretagne_titles = []; bretagne_descriptions = []; bretagne_dates= []
bretagne= {"bretagne_titles":bretagne_titles, "bretagne_descriptions":bretagne_descriptions, "bretagne_dates":bretagne_dates}
for i,j in bretagne.items():
    open_info(j,i)

centre_titles = []; centre_descriptions = []; centre_dates= []
centre= {"centre_titles":centre_titles, "centre_descriptions":centre_descriptions, "centre_dates":centre_dates}
for i,j in centre.items():
    open_info(j,i)

delinquance = ["criminalite","delinquant","prevention","violence","violent","juvenile","delit","insecurite","criminologie","securite","police","delinquance","juvenile","penal","crime","videosurveillance","banditisme","reinsertion","malfaiteur","hooligan","repression","quartier","judiciaire","racaille"]

environnement_cat_nat = ["seisme","sinistre","cataclysme","risque naturel","tremblement de terre","famine","inondation","canicule","secheresse","tsunami","calamite naturelle","fleau","nature","force majeure","solidarit","ecologique","protection","espece","disparition","menace","rechauffement","climatique","climat","tornade","ouragan","habitat","extinction"]

environnement = ["ecologie","pollution","environnement","ecologique","preservation","degradation","ecosysteme","biodiversite","nature","durable","ecologiste","dechet","developpement durable","recyclage","habitat","biosphere","polluant","faune","polluer","preserver","pesticide","conservation","contamination","vegetal","climatique","ressource","temperature","energetique","agriculture","toxique","nucleaire","energie","renouvelable","deforestation","biologie","marin","OGM"]

europe = ["europe","ue","europeen","europa","mediterranee","union europeenne","vieux continent","bruxelles","commission","cee","euro","franco-allemand","allemagne","luxembourg","europhile","balkan","brexit","belgique","italie","espagne","portugal","pologne","hongrie","chypre","irlande","slovenie","slovaquie","otan","grece","scandinavie","bulgarie","autriche","suede","finlande","danemark","pfue"]

pouvoir_dachat = ["hausse","salaire","consommation","niveau de vie","augmente","baisse","diminution","prix","inflation","monnaie","TVA","devaluation","retraite","revenus","erosion","actifs","appauvrissement","augmentation","baisser","battent","carburant","chomage","classes moyennes","cotisation","cotisations sociales","coup de pouce","croissance","depenses","dette","diminue","exoneration","fiscale","fiscalite","gain","hausse des prix","importes","impot","inegalites","invalidite","loyers","mnages","mesures","minimum vieillesse","modestes","mutuelles","pensions","perte","retraites","salaries","taxe","dhabitation","impot"]

education = ["enseignement","instruction","pedagogie","apprentissage","scolaire","educatif","educateur","formation","culture","primaire","scolarisation","secondaire","eduquer","jeunesse","alphabetisation","universitaire","enseignant","pedagogue","prescolaire","college","discipline","parent","precepteur","baccalaureat","pedagogique","connaissance","intellectuelle","lycee","etablissement","scolarite","ecole","universite","civique","instituteur","bourse","professeur"]

violence_aux_femmes = ["feminicide","sexiste","sexisme","discrimination","machisme","misogynie","feminisme","phallocratie","harcelement","viol","sexuelle","macho"]

emploi = ["employeur","chomage","salarie","travail","poste","embauche","insertion","job","service","chomeur","secteur","profession","salaire","croissance","demandeur","remuneration","agence","employe","handicap","travailleur","promotion","remunere","allocation","saisonnier","assurance","economique","population active","precaire","smic","tertiaire","revenu","pole emploi","pole","cdi","cdd","stage","stagiaire","interim","alternant","alternance","anpe","postuler","cumul","cotisation","productivite","produire","candidature","pme","startup","recruter","doeuvre","main doeuvre","capital","profession","professionnel","solidarite","demissionner","inactivite"]

retraite = ["retraite","pension","preretraite","cotisation","vieillesse","aide","ehpad","agee"]

industrie = ["industrie","manufacture","ouvrier","usine","textile","automobile","aerospatiale","production","metallurgie","industrialisation","industrielle","forge","acier","acierie","aluminium","petrochimique","petrochimique","travailleur","fer"]

transport = ["transport","metro","train","avion","voiture","autouroute","peripherique","circulation","trajet","tgv","essence","bus","car","automobile","velo","cyclabe","pieton","ter","rer","tram","tramway","ferroviaire","sncf","ratp","air france","aerien","deplacement"]

immigration = ["immigration","immigrant","immigre","migration","sans papier","identite","clandestin",\
               "clandestine","asile","migration","assimilation","integration","demographique","ethnique",\
               "refugies","naturalisation","multiculturalisme","demographie","frontiere"]

economie = ["budget","budgetaire","budgets","budgetaires","monetaire","prosperite","economie","croissance","entreprise","productivite","investissement","startup","revenu","activite"\
           "innovation","developpement","industriel","richesse","macroeconomie","emploi","capital","chomage","dette","crise","competitivite"\
           "credit","pret","redressement","faillite","attractivite","impot","impots"]

securite = ["arme",'vol',"policier","policiers","poignarde","homicide","dhomicide","dangereux","dangereuse","terrorisme","protection","securite","surete","defense","securitaire","police","armee","renforcer"\
           "cooperation","vol","delinquance","securise","menacer","viol","menace","urgence","penal","piratage"\
           "criminalite","vigilance","loi","securitarisme","tue","tuer"]

gouvernement = ["demission","remaniement","president","justice","gouvernement","gouvernemental","parlementaire","parlement","depute","senateur","remaniement","conseil","constitution","constitutionnel","autorite","republique","politique","executif","lexecutif","parlement","administration","ladministration","ministere","etat","letat","oligarchie","loligarchie","opposition","lopposition","provincial","ministre","premier","ministre","ministres","conseiller","aristocratie","laristocratie","gouvernemental","pouvoir","democratie","monarchie","federal","provisoire","republicain","democratie","democratique","totalitaire","autoritaire","nationale","nation"]

vaccin = ["negatif","positif","dose","vaccin","vaccins","covid","risque","cas","malade","reanimation","hopitaux","medecins","hopital","medecin","infirmier","infirmiers","vaccinal","test","omicron","domicron","test","tests","depistage","sante","sanitaire","pandemie","virus","oms","passe","variant"]

candidats = ["eric","zemmour","marine","lepen","pen","emmanuel","macron","valerie","pecresse","anne","hidalgo","jean","luc","jeanluc","melenchon","jadot","yannick","nicolas","dupont","aignan","dupontaignan"]

topics = [immigration, economie, securite, gouvernement, vaccin, candidats,delinquance,
        environnement_cat_nat,environnement, europe, pouvoir_dachat,education,violence_aux_femmes,emploi,retraite,industrie,transport]

zemmour = ["eric","zemmour","reconquete"]
lepen = ["marine","pen","lepen","rassemblement national","rassemblement","rn"]
macron = ["emmanuel","macron","president","en marche","lrem","marche"]
pecresse = ["valerie","pecresse","lesrepublicains","lr","republicains"]
hidalgo = ["ps","anne","hidalgo","socialiste"]
melenchon = ["melenchon","jeanluc","lfi","insoumis"]
jadot = ["yannick","jadot","verts"]
autres = ["poutou","taubira","dupontaignan","aignan","roussel","arthaud","kazib","montebourg","waechter","philippot","asselineau","martinez","lassalle","thouy","langlois"]
candidates = [zemmour, lepen, macron, pecresse, hidalgo, melenchon, jadot, autres]

a_titles = [normandie_titles,nord_titles,est_titles,bourgogne_titles,auvergne_titles,
paca_titles, occitanie_titles, leparisien_titles, aquitaine_titles, loire_titles, bretagne_titles, centre_titles]
a_descriptions = [normandie_descriptions, nord_descriptions, est_descriptions, bourgogne_descriptions, auvergne_descriptions,
paca_descriptions, occitanie_descriptions,leparisien_descriptions,
aquitaine_descriptions, loire_descriptions, bretagne_descriptions, centre_descriptions]


topics_count = []
for i in range(0,len(a_titles)):
    regional_count = stuff_topics(a_titles[i],a_descriptions[i],topics)
    topics_count.append(regional_count)

#To get PCT per region
topics_count_pct = []
for i in range(0,12):
    petite_count = []
    petite_count2 = []
    for j in range(0,17):
        petite_count.append(topics_count[i][j])
    for i in petite_count:
        petite_count2.append(i/(sum(petite_count)-petite_count[4])*100)
    topics_count_pct.append(petite_count2)

#plot(get_viz_df(topics_count_pct))


APP_NAME = "Analyse PQR"
st.markdown("<h1 style='text-align: center; color: black;'Analyse PQR</h1>", unsafe_allow_html=True)


st.write(plot(get_viz_df(topics_count_pct)))
st.write(plot_candidates(get_viz_candidates(candidates, a_titles, a_descriptions)))
