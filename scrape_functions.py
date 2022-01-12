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

def scrape_parisnormandie():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    driver.get(f'https://www.paris-normandie.fr/')

    driver.implicitly_wait(random.randrange(1, 4))
    driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div/div/div[3]/button")[1].click()

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get urls
    results = soup.find_all(class_="media-heading")

    for i in results:
        try:
            urls.append(f'https://www.paris-normandie.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    urls = check_duplicates(urls)
    print("Paris-Normandie", (len(urls)))
    for count, i in enumerate(urls):
        if "emplois.leschasseursdemploi" not in i:
            progressBar(count,len(urls),barLength = 20)
            driver.get(i)
            driver.implicitly_wait(random.randrange(1, 5))

            ## In case Clicking is required
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            try:
                descriptions.append(soup.find("meta", {"name":"description"})["content"])
            except TypeError:
                descriptions.append(0)
            keywords.append(soup.find("meta", {"name":"keywords"})["content"])
            titles.append(soup.find("meta", {"property":"og:title"})["content"])
            date = soup.find("meta", {"property":"article:published_time"})["content"]
            dates.append(pd.to_datetime(date.strip()[:16], format="%Y-%m-%dT%H:%M"))

    return (titles,descriptions,dates,driver,keywords)

def scrape_lamanchelibre():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    driver.get(f'https://www.lamanchelibre.fr/')

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get main url
    urls.append(soup.find(class_="col-lg-8 left-article article_obj articlePrincipal").find("a")["href"])

    #get secondary urls
    results = soup.find_all(class_="article_obj")
    for i in results:
        try:
            urls.append(i.find("a")["href"])
        except TypeError:
            pass

    #get other urls
    results = soup.find_all(class_="minArticle")
    for i in results:
        try:
            urls.append(i.find("a")["href"])
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    undesirables = ['https://www.lamanchelibre.fr/inscription-newsletter/', 'https://www.lamanchelibre.fr/abonnement/', 'https://www.lamanchelibre.fr/agenda-sorties.html', 'https://annonces.lamanchelibre.fr', 'https://www.lamanchelibre.fr/en-continu/la-petite-manche-libre/', 'https://www.lamanchelibre.fr/communes.html', 'https://www.lamanchelibre.fr/rubrique/loisir/sortie/', 'https://www.lamanchelibre.fr/tag/commerce/', 'https://www.lamanchelibre.fr/rubrique/sport/']
    for i in undesirables:
        urls.remove(i)
    urls = check_duplicates(urls)
    print("La Manche Libre", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 5))

        ## In case Clicking is required
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"name":"description"})["content"])
        except TypeError:
            descriptions.append(0)

        #Titles
        titles.append(soup.find("meta", {"name":"title"})["content"])

        #Convert Date
        date = soup.find(class_="article_date_pub").text
        date = date.replace("Publié le ","").replace(" à","").replace("h",":")
        dates.append(pd.to_datetime(date.strip()[:16], format="%d/%m/%Y %H:%M"))

    return titles,descriptions,dates,driver

def scrape_lavoixdunord():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')

    driver.get(f'https://www.lavoixdunord.fr/')

    driver.implicitly_wait(random.randrange(1, 4))
    driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div/div/div[3]/button")[1].click()

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get main url
    results = soup.find_all(class_="media-heading")
    for i in results:
        if f'https://www.lavoixdunord.fr{i.find("a")["href"]}'.startswith("https://www.lavoixdunord.frhttp"):
            pass
        else:
            urls.append(f'https://www.lavoixdunord.fr{i.find("a")["href"]}')

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    urls = check_duplicates(urls)
    print("La Voix du Nord", (len(urls)))

    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 5))

        ## In case Clicking is required
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"property":"og:description"})["content"])
        except TypeError:
            descriptions.append(0)

        #Titles
        try:
            titles.append(soup.find("meta", {"property":"og:title"})["content"])
        except TypeError:
            descriptions.append(0)

        #Convert Date
        date = soup.find("meta", {"property":"article:published_time"})["content"]
        dates.append(pd.to_datetime(date.strip()[:16], format="%Y/%m/%dT%H:%M"))
    driver.quit()
    return titles,descriptions,dates,driver

def scrape_nordeclair():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')

    driver.get(f'https://www.nordeclair.fr/')
    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get urls
    results = soup.find_all(class_="media-heading")
    for i in results:
        try:
            if f'https://www.nordeclair.fr{i.find("a")["href"]}'.startswith("https://www.nordeclair.frhttp"):
                pass
            else:
                urls.append(f'https://www.nordeclair.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    for i in urls:
        if 'https://www.nordeclair.frhttps/' in i:
            urls.remove(i)
    urls = check_duplicates(urls)
    print("Nord Eclair", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 5))

        ## In case Clicking is required
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"property":"og:description"})["content"])
        except TypeError:
            descriptions.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        date = soup.find("meta", {"property":"article:published_time"})["content"]
        dates.append(pd.to_datetime(date.strip()[:16], format="%Y/%m/%dT%H:%M"))

    return titles,descriptions,dates

def scrape_courrierpicard():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    driver.get(f'https://www.courrier-picard.fr/')
    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get urls
    results = soup.find_all(class_="media-heading")
    for i in results:
        try:
            if f'https://www.courrier-picard.fr{i.find("a")["href"]}'.startswith("https://www.courrier-picard.frhttp"):
                pass
            else:
                urls.append(f'https://www.courrier-picard.fr{i.find("a")["href"]}')
        except TypeError:
            pass
    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    for i in urls:
        if 'https://www.courrier-picard.frhttps/' in i:
            urls.remove(i)
    urls = check_duplicates(urls)
    print("Courrier Picard", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 5))

        ## In case Clicking is required
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find(class_="description")["content"])
        except TypeError:
            descriptions.append(0)

        keywords.append(soup.find("meta", {"name":"keywords"})["content"])

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        date = soup.find("meta", {"property":"article:published_time"})["content"]
        dates.append(pd.to_datetime(date.strip()[:16], format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates

def scrape_estrepublicain():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    driver.get(f'https://www.estrepublicain.fr/')
    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get primary urls
    urls.append(f'https://www.estrepublicain.fr{soup.find(class_="primary RichContent").find("a")["href"]}')

    #get secondary urls
    results = soup.find_all(class_="secondary RichContent")
    for i in results:
        try:
            urls.append(f'https://www.estrepublicain.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    urls = check_duplicates(urls)
    print("Est Républicain", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 5))

        ## In case Clicking is required
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"name":"Description"})["content"])
        except TypeError:
            descriptions.append(0)

        try:
            keywords.append(soup.find("meta", {"name":"Keywords"})["content"])
        except TypeError:
            keywords.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        dct = json.loads(soup.find("script",type="application/ld+json").string)
        dates.append(pd.to_datetime(dct["datePublished"],format="%Y-%m-%dT%H:%M"))
        #date = soup.find(class_="date").text.replace("lun.","").replace("mar.","").replace("mer.","").replace("jeu.","").replace("ven.","").replace("sam.","").replace("dim.","di")
        #dates.append(pd.to_datetime(date.strip()[:10], format="%d/%m/%Y"))

    return titles,descriptions,dates,driver,keywords

def scrape_dna(driver):
    driver.get(f'https://www.dna.fr/')

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get primary urls
    results = soup.find_all(class_="primary RichContent")
    for i in results:
        try:
            urls.append(f'https://www.dna.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get secondary urls
    results = soup.find_all(class_="secondary RichContent")
    for i in results:
        try:
            urls.append(f'https://www.dna.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    urls = check_duplicates(urls)
    print("Dernières Nouvelles D'Alsace", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 5))

        ## In case Clicking is required
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"name":"Description"})["content"])
        except TypeError:
            descriptions.append(0)

        try:
            keywords.append(soup.find("meta", {"name":"Keywords"})["content"])
        except TypeError:
            keywords.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        dct = json.loads(soup.find("script",type="application/ld+json").string)
        dates.append(pd.to_datetime(dct["datePublished"],format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver,keywords

def scrape_lunion():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    driver.get(f'https://www.lunion.fr/')

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get primary urls
    results = soup.find_all(class_="media-heading")
    for i in results:
        try:
            if "francelive" not in i.find("a")["href"] and i.find("a")["href"] != "https://www.lunion.fr":
                urls.append(f'https://www.lunion.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    new_urls = []
    for i in urls:
        if i != "https://www.lunion.fr".strip():
            new_urls.append(i)
    urls = new_urls
    urls = check_duplicates(urls)
    print("L'Union L'Ardennais", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 5))

        ## In case Clicking is required
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"name":"description"})["content"])
        except TypeError:
            descriptions.append(0)

        try:
            keywords.append(soup.find("meta", {"name":"keywords"})["content"])
        except TypeError:
            keywords.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        date = soup.find("meta", {"property":"article:published_time"})["content"]
        dates.append(pd.to_datetime(date.strip()[:16], format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver,keywords

def scrape_lorrain():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    #driver.delete_all_cookies()
    #driver.get("chrome://settings/clearBrowserData")
    driver.get(f'https://www.republicain-lorrain.fr/')

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get primary urls
    results = soup.find_all(class_="primary RichContent")
    for i in results:
        try:
            urls.append(f'https://www.republicain-lorrain.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get secondary urls
    results = soup.find_all(class_="secondary RichContent")
    for i in results:
        try:
            urls.append(f'https://www.republicain-lorrain.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    urls = check_duplicates(urls)
    print("Le Républicain Lorrain", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 5))

        ## In case Clicking is required
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"name":"Description"})["content"])
        except TypeError:
            descriptions.append(0)

        try:
            keywords.append(soup.find("meta", {"name":"Keywords"})["content"])
        except TypeError:
            keywords.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        dct = json.loads(soup.find("script",type="application/ld+json").string)
        dates.append(pd.to_datetime(dct["datePublished"],format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver,keywords

def scrape_lalsace(driver):
    driver.get(f'https://www.lalsace.fr/')

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get primary urls
    results = soup.find_all(class_="primary RichContent")
    for i in results:
        try:
            urls.append(f'https://www.lalsace.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get secondary urls
    results = soup.find_all(class_="secondary RichContent")
    for i in results:
        try:
            urls.append(f'https://www.lalsace.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    urls = check_duplicates(urls)
    print("L'Alsaceb", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 5))

        ## In case Clicking is required
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"name":"Description"})["content"])
        except TypeError:
            descriptions.append(0)

        try:
            keywords.append(soup.find("meta", {"name":"Keywords"})["content"])
        except TypeError:
            keywords.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        dct = json.loads(soup.find("script",type="application/ld+json").string)
        dates.append(pd.to_datetime(dct["datePublished"],format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver,keywords

def scrape_lyonne():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    #driver.delete_all_cookies()
    driver.get(f'https://www.lyonne.fr/')

    driver.implicitly_wait(random.randrange(1, 4))
    driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div/div/div[3]/button")[1].click()
    #driver.implicitly_wait(random.randrange(1, 3))
    #driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/button").click()

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get urls
    results = soup.find_all(class_="custom-hover")
    for i in results:
        try:
            urls.append(f'https://www.lyonne.fr{i["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    urls = check_duplicates(urls)
    print("L'Yonne", (len(urls)))

    for count, i in enumerate(urls):
        i = i.replace("https://www.lyonne.frhttps://www.lyonne.fr","https://www.lyonne.fr")
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 5))

        ## In case Clicking is required
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"name":"description"})["content"])
        except TypeError:
            descriptions.append(0)

        try:
            keywords.append(soup.find("meta", {"name":"keywords"})["content"])
        except TypeError:
            keywords.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        date = soup.find("meta", {"property":"article:published_time"})["content"]
        dates.append(pd.to_datetime(date.strip()[:16], format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver,keywords

def scrape_lejsl(driver):
    driver.get(f'https://www.lejsl.com/')

    #driver.implicitly_wait(random.randrange(1, 4))
    #driver.find_elements_by_xpath("/html/body/div[6]/div/div/div[2]/button").click()
    #driver.implicitly_wait(random.randrange(1, 3))
    #driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/button").click()

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get primary urls
    results = soup.find_all(class_="primary RichContent")
    for i in results:
        try:
            urls.append(f'https://www.lejsl.com{i.find("a")["href"]}')
        except TypeError:
            pass

    #get secondary urls
    results = soup.find_all(class_="secondary RichContent")
    for i in results:
        try:
            urls.append(f'https://www.lejsl.com{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    urls = check_duplicates(urls)
    print("Le Journal de Saone et Loire", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 5))

        ## In case Clicking is required
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"name":"Description"})["content"])
        except TypeError:
            descriptions.append(0)

        try:
            keywords.append(soup.find("meta", {"name":"Keywords"})["content"])
        except TypeError:
            keywords.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        dct = json.loads(soup.find("script",type="application/ld+json").string)
        dates.append(pd.to_datetime(dct["datePublished"],format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver,keywords

def scrape_bienpublic(driver):
    driver.get(f'https://www.bienpublic.com/')

    #driver.implicitly_wait(random.randrange(1, 4))
    #driver.find_elements_by_xpath("/html/body/div[6]/div/div/div[2]/button").click()
    #driver.implicitly_wait(random.randrange(1, 3))
    #driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/button").click()

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get primary urls
    results = soup.find_all(class_="primary RichContent")
    for i in results:
        try:
            urls.append(f'https://www.bienpublic.com{i.find("a")["href"]}')
        except TypeError:
            pass

    #get secondary urls
    results = soup.find_all(class_="secondary RichContent")
    for i in results:
        try:
            urls.append(f'https://www.bienpublic.com{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    urls = check_duplicates(urls)
    print("Le Bien Public", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 5))

        ## In case Clicking is required
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"name":"Description"})["content"])
        except TypeError:
            descriptions.append(0)

        try:
            keywords.append(soup.find("meta", {"name":"Keywords"})["content"])
        except TypeError:
            keywords.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        dct = json.loads(soup.find("script",type="application/ld+json").string)
        dates.append(pd.to_datetime(dct["datePublished"],format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver,keywords
def scrape_leprogres():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    #driver.delete_all_cookies()
    driver.get(f'https://www.leprogres.fr/')

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get main urls
    results = soup.find_all(class_="primary RichContent")
    for i in results:
        try:
            urls.append(f'https://www.leprogres.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get secondary urls
    results = soup.find_all(class_="secondary RichContent")
    for i in results:
        try:
            urls.append(f'https://www.leprogres.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    urls = check_duplicates(urls)
    print("Le Progrès", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 4))
        try:
            driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div/div/div[3]/button")[0].click()
        except IndexError:
            pass
        driver.implicitly_wait(random.randrange(1, 2))
        try:
            driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/button")[0].click()
        except IndexError:
            pass
        ## In case Clicking is required
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"name":"Description"})["content"])
        except TypeError:
            descriptions.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        try:
            date = soup.find("meta", {"property":"article:published_time"})["content"]
            dates.append(pd.to_datetime(date.strip()[:16], format="%Y-%m-%dT%H:%M"))
        except TypeError:
            pass
        try:
            dct = json.loads(soup.find("script",type="application/ld+json").string)
            dates.append(pd.to_datetime(dct["datePublished"],format="%Y-%m-%dT%H:%M"))
        except TypeError:
            pass

    return titles,descriptions,dates,driver

def scrape_lamontagne():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    #driver.delete_all_cookies()
    driver.get(f'https://www.lamontagne.fr/')

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get main urls
    results = soup.find_all(class_="c-titre la")
    for i in results:
        try:
            urls.append(f'https://www.lamontagne.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get secondary urls
    results = soup.find_all(class_="c-titre")
    for i in results:
        try:
            urls.append(f'https://www.lamontagne.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    new_urls = []
    for url in urls:
        if str(url).startswith("https://www.lamontagne.fr/gf"):
            pass
        elif str(url).startswith("https://www.lamontagne.fr/theme/"):
            pass
        elif str(url).startswith("https://www.lamontagne.frhttps//www.lamontagne.fr"):
            pass
        elif str(url).startswith("https://www.lamontagne.frhttps://www.lamontagne.fr"):
            pass
        else:
            new_urls.append(url)
    urls = new_urls
    urls = check_duplicates(urls)
    print("La Montagne", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 4))

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"name":"description"})["content"])
        except TypeError:
            descriptions.append(0)

        try:
            keywords.append(soup.find("meta", {"name":"keywords"})["content"])
        except TypeError:
            keywords.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        try:
            date = soup.find("meta", {"property":"article:published_time"})["content"]
            dates.append(pd.to_datetime(date.strip()[:16], format="%Y-%m-%dT%H:%M"))
        except TypeError:
            dct = json.loads(soup.find("script",type="application/ld+json").string)
            dates.append(pd.to_datetime(dct["datePublished"],format="%Y-%m-%dT%H:%M"))


    return titles,descriptions,dates,driver, keywords


def scrape_laprovence():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    #driver.delete_all_cookies()
    driver.get(f'https://www.laprovence.com/')

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get main urls
    results = soup.find_all(class_="section-teaser-item__text-wrapper section-teaser-item__text-wrapper--text-dark")
    for i in results:
        try:
            urls.append(f'https://www.laprovence.com{i.find(class_="xiticlick")["href"]}')
        except TypeError:
            pass

    #get slider urls
    results = soup.find_all(class_="slider__item")
    for i in results:
        try:
            urls.append(f'https://www.laprovence.com{i.find("a")["href"]}')
        except TypeError:
            pass

    results = soup.find_all(class_="section-item__text-wrapper section-item__text-wrapper--text-dark section-item__text-wrapper--alt")
    for i in results:
        try:
            urls.append(f'https://www.laprovence.com{i.find(class_="xiticlick")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    undesirables = ["https://www.laprovence.comhttps//www.laprovence.com/actualites",'https://www.laprovence.comhttps://www.laprovence.com/om', 'https://www.laprovence.comhttps://www.laprovence.com/sports', 'https://www.laprovence.comhttps://www.laprovence.com/politique', 'https://www.laprovence.comhttps://www.laprovence.com/faits-divers-justice', 'https://www.laprovence.comhttps://www.laprovence.com/faits-divers-justice', 'https://www.laprovence.comhttps://www.laprovence.com/faits-divers-justice', 'https://www.laprovence.comhttps://www.laprovence.com/faits-divers-justice', 'https://www.laprovence.comhttps://www.laprovence.com/sante', 'https://www.laprovence.comhttps://www.laprovence.com/societe']
    for i in undesirables:
        try:
            urls.remove(i)
        except ValueError:
            pass
    new_urls = []
    for url in urls:
        if str(url).startswith("https://www.laprovence.comhttps://www.laprovence.com"):
            pass
        else:
            new_urls.append(url)
    urls = new_urls
    urls = check_duplicates(urls)
    print("La Provence", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 4))


        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"itemprop":"description"})["content"])
        except TypeError:
            descriptions.append(0)

        try:
            keywords.append(soup.find("meta", {"name":"keywords"})["content"])
        except TypeError:
            keywords.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        date = soup.find("time")["datetime"]
        dates.append(pd.to_datetime(date.strip()[:16], format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver,keywords

def scrape_nicematin():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    #driver.delete_all_cookies()
    driver.get(f'https://www.nicematin.com/')

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get main urls
    results = soup.find_all(class_="article-preview bigger")
    for i in results:
        try:
            urls.append(i.find("a")["href"])
        except TypeError:
            pass

    #get slider urls
    results = soup.find_all(class_="rearrange")
    for i in results:
        try:
            urls.append(i.find("a")["href"])
        except TypeError:
            pass

        results = soup.find_all(class_="desc")
        try:
            urls.append(i.find("a")["href"])
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    urls = check_duplicates(urls)
    print("Nice-Matin", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 4))

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"name":"description"})["content"])
        except TypeError:
            descriptions.append(0)

        #try:
            #keywords.append(soup.find("meta", {"name":"keywords"})["content"])
        #except TypeError:
            #keywords.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        date = soup.find("meta", {"property":"article:published_time"})["content"]
        dates.append(pd.to_datetime(date.strip()[:16], format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver

def scrape_varmatin():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    #driver.delete_all_cookies()
    driver.get(f'https://www.varmatin.com/')

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get main urls
    results = soup.find_all(class_="article-preview bigger")
    for i in results:
        try:
            urls.append(i.find("a")["href"])
        except TypeError:
            pass

    #get slider urls
    results = soup.find_all(class_="rearrange")
    for i in results:
        try:
            urls.append(i.find("a")["href"])
        except TypeError:
            pass

    results = soup.find_all(class_="desc")
    for i in results:
        try:
            urls.append(i.find("a")["href"])
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    new_urls = []
    for i in urls:
        if i not in new_urls:
            new_urls.append(i)
    urls = new_urls
    urls = check_duplicates(urls)
    print("Var Matin", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 4))

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
        date = soup.find("meta", {"property":"article:published_time"})["content"]
        dates.append(pd.to_datetime(date.strip()[:16], format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver

def scrape_midilibre():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    #driver.delete_all_cookies()
    driver.get(f'https://www.midilibre.fr/')

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get main urls
    results = soup.find_all(class_="article__title")
    for i in results:
        try:
            urls.append(f'https://www.midilibre.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    urls = check_duplicates(urls)
    print("Midi Libre", (len(urls)))
    for count, i in enumerate(urls):
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

        #try:
            #keywords.append(soup.find("meta", {"name":"keywords"})["content"])
        #except TypeError:
            #keywords.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        dct = json.loads(soup.find("script",type="application/ld+json").string)
        dates.append(pd.to_datetime(dct["datePublished"],format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver

def scrape_lindependant():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    #driver.delete_all_cookies()
    driver.get(f'https://www.lindependant.fr')

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get main urls
    results = soup.find_all(class_="article__title")
    for i in results:
        try:
            if "immobilier" not in i.find("a")["data-xiti-action"]:
                urls.append(f'https://www.lindependant.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    urls = check_duplicates(urls)
    print("L'indépendant", (len(urls)))
    for count, i in enumerate(urls):
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

        #try:
            #keywords.append(soup.find("meta", {"name":"keywords"})["content"])
        #except TypeError:
            #keywords.append(0)

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        date = soup.find("time")["content"]
        dates.append(pd.to_datetime(date.strip()[:16], format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver

def scrape_leparisien():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    #driver.delete_all_cookies()
    driver.get("https://www.leparisien.fr/info-paris-ile-de-france-oise/")

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get Articles
    urls.append(soup.find(class_="story-preview story-text-bottom text-bottom-for-mobile flex-feed-unit dropcap-unit").find("a")["href"].replace("//","https://"))

    for i in soup.find_all(class_="six-chain flex-feed display-horizontal container-col-12"):
        if i.find("a")["href"].replace("//","https://").startswith("https://www.leparisien.fr/podcasts"):
            pass
        else:
            urls.append(i.find("a")["href"].replace("//","https://"))

    for i in soup.find_all(class_="flex-feed container-col-4 feed-text-bottom"):
        if i.find("a")["href"].replace("//","https://").startswith("https://www.leparisien.fr/podcasts"):
            pass
        else:
            urls.append(i.find("div").find("a")["href"].replace("//","https://"))

    for i in soup.find_all(class_="story-preview story-text-bottom text-right-for-mobile flex-feed-unit"):
        if i.find("a")["href"].replace("//","https://").startswith("https://www.leparisien.fr/podcasts"):
            pass
        else:
            urls.append(i.find("a")["href"].replace("//","https://"))

    for i in soup.find_all(class_="story-preview story-text-right text-right-for-mobile flex-feed-unit"):
        if i.find("a")["href"].replace("//","https://").startswith("https://www.leparisien.fr/podcasts"):
            pass
        else:
            urls.append(i.find("a")["href"].replace("//","https://"))

    #get titles and descriptions
    titles  = []
    article_desc = []
    dates = []
    urls = check_duplicates(urls)
    print("Le Parisien", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 8))

        ## In case Clicking is required
        #try:
            #driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[3]/button").click()
        #except "NoSuchElementException":
            #pass

        #Other Click
        #driver.implicitly_wait(random.randrange(1, 5))

        #try :
            #driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/button").click()
        #except "NoSuchElementException":
            #pass

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        article_desc.append(soup.find("meta", {"name":"description"})["content"])
        titles.append(soup.find("title").text)


        #Converting to Datetime
        date = soup.find(class_="timestamp width_full margin_top_ten ui").text
        date = date.split(",")
        date = date[0][3:].replace("à","").strip().lower()
        date = date.replace(" décembre ","/12/").replace(" novembre ","/11/").replace(" janvier ","/01/").replace(" février ","/02/").replace(" mars ","/03/").replace(" avril ","/04/").replace(" mai ","/05/").replace(" mai ","/06/").replace(" juin ","/06/").replace(" juillet ","/07/").replace(" août ","/08/").replace(" septembre ","/09/").replace(" octobre ","/10/").replace("  "," ").replace("h",":")
        date = pd.to_datetime(date.strip(), format="%d/%m/%Y %H:%M")
        dates.append(date)

    return (titles,article_desc,dates, driver)

def scrape_ladepeche():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    #driver.delete_all_cookies()
    driver.get(f'https://www.ladepeche.fr/')

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get main urls
    results = soup.find_all(class_="article__title")
    for i in results:
        try:
            if "https://www.ladepeche.fr/2022/01/06/toulouse-une-formation" in f'https://www.ladepeche.fr{i.find("a")["href"]}':
                    pass
            else:
                urls.append(f'https://www.ladepeche.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    urls = check_duplicates(urls)
    print("La Depeche", (len(urls)))
    for count, i in enumerate(urls):
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
        date = soup.find("time")["content"]
        dates.append(pd.to_datetime(date.strip()[:16], format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver

def scrape_sudouest():
    options = Options()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"')
    #driver.delete_all_cookies()
    driver.get(f'https://www.sudouest.fr/')

    #get_code
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    urls = []

    #get main urls
    results = soup.find_all(class_="inner-article")
    for i in results:
        try:
            if "youtube" in f'{i.find("a")["href"]}':
                pass
            else:
                urls.append(f'https://www.sudouest.fr{i.find("a")["href"]}')
        except TypeError:
            pass

    #get titles and descriptions
    titles  = []
    descriptions = []
    keywords = []
    dates = []
    for i in urls:
        if "notre-dossier" in i or "youtube" in i:
            urls.remove(i)
    try:
        urls.remove('https://www.sudouest.fr/formats-longs/')
        urls.remove("https://www.sudouest.fr/economie/immobilier/immobilier-en-gironde-coliving-coloc-ces-nouvelles-facons-de-se-loger-7461796.php")
    except ValueError:
        pass
    urls = check_duplicates(urls)
    print("Sud Ouest", (len(urls)))
    for count, i in enumerate(urls):
        progressBar(count,len(urls),barLength = 20)
        driver.get(i)
        driver.implicitly_wait(random.randrange(1, 4))


        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Descriptions
        try:
            descriptions.append(soup.find("meta", {"name":"description"})["content"])
        except TypeError:
            descriptions.append(0)

        keywords.append(soup.find("meta", {"name":"news_keywords"})["content"])

        #Titles
        titles.append(soup.find("meta", {"property":"og:title"})["content"])

        #Convert Date
        date = soup.find("time")["datetime"]
        dates.append(pd.to_datetime(date.strip()[:16], format="%Y-%m-%dT%H:%M"))

    return titles,descriptions,dates,driver, keywords

