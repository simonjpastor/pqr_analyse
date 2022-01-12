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
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import json
import plotly.express as px
import streamlit as st



APP_NAME = "Analyse PQR"
st.markdown("<h1 style='text-align: center; color: black;'Analyse PQR</h1>", unsafe_allow_html=True)

y = pd.read_csv("y.csv", index_col=0)
x = pd.read_csv("x.csv",index_col=0)

y = y.reset_index()

APP_NAME = "Analyse PQR"
st.markdown("<h1 style='text-align: center; color: black;'Analyse PQR</h1>", unsafe_allow_html=True)

st.write(plot(x))
st.write(plot_candidates(y))
