from general_functions import progressBar, check_date, check_duplicates, tokenize, count_func, \
day_word, topic_count, topic_count2, stuff_topics, get_viz_df, plot, gen_driver
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

#driver = gen_driver()

def scrape_ouestfrance1(driver,link):
    driver.get(link)

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []
    #get main urls
    results = soup.find_all(class_="titre-lien")
    for i in results:
        try:
            if str(i["href"]).startswith("https://www.ouestfrance-immo.com"):
                pass
            elif str(i["href"]).startswith("https://www.ouestfrance-auto.com"):
                pass
            elif str(i["href"]).startswith("https://www.ouestfrance-emploi.com/"):
                pass
            elif str(i["href"]).startswith("https://infolocale.ouest-france.fr/"):
                pass
            elif str(i["href"]).startswith("https://agence-api.ouest-france.fr/"):
                pass
            elif str(i["href"]).startswith("https://madeinfoot.ouest-france.fr/"):
                pass
            elif str(i["href"]).startswith("https://vin-champagne.ouest-france.fr"):
                pass
            elif str(i["href"]).startswith("https://partir.ouest-france.fr"):
                pass
            elif str(i["href"]).startswith("https://www.ouest-france.fr/partenariats-ouest-france"):
                pass
            elif str(i["href"]).startswith("https://bricoleurpro.ouest-france.fr"):
                pass
            elif "francelive" in str(i["href"]):
                pass
            else:
                urls.append(i["href"])
        except TypeError:
            pass

    for i in urls:
        if "https://www.ouest-france.fr/leditiondusoi" in str(i):
            urls.remove(i)
        elif "https://www.ouestfrance-immo.com/" in str(i):
            urls.remove(i)
    urls = check_duplicates(urls)
    return urls

def scrape_ouestfrance2(driver, urls):
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    print((len(urls)))
    for count, i in enumerate(urls) :
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 4))
        #try:
            #driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div/div/div[3]/button")[0].click()
        #except IndexError:
            #pass
        #driver.implicitly_wait(random.randrange(1, 2))
        #try:
            #driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/button")[0].click()
        #except IndexError:
            #pass

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"name":"description"})["content"])
        except TypeError:
            descriptions.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        date = soup.find(class_="meta-time")["datetime"]
        dates.append(pd.to_datetime(date.strip()[:16], format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver

###Presse Océane
urls = scrape_ouestfrance1(driver, "https://www.ouest-france.fr/presse-ocean/")
presseoceane_titles, presseoceane_descriptions, presseoceane_dates, driver  = scrape_ouestfrance2(driver, urls[:int(round(len(urls)/4,0))])
