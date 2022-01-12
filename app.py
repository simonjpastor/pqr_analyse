from scrape_functions import scrape_parisnormandie,scrape_lamanchelibre,scrape_lavoixdunord, scrape_nordeclair, scrape_lunion, scrape_courrierpicard,scrape_estrepublicain, scrape_dna, scrape_lunion, scrape_lorrain, scrape_lalsace,scrape_lyonne, scrape_lejsl, scrape_bienpublic, scrape_leprogres, scrape_lamontagne, scrape_laprovence, scrape_nicematin, scrape_varmatin, scrape_midilibre, scrape_lindependant, scrape_leparisien, scrape_ladepeche, scrape_sudouest

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
import pandas as pd
import streamlit as st

APP_NAME = "Consulting Job Search"

st.title(APP_NAME)

st.write(plot(get_viz_df(topics_count_pct)))
