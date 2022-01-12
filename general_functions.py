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

def progressBar(current, total, barLength = 20):
    percent = float(current) * 100 / total
    arrow   = '-' * int(percent/100 * barLength - 1) + '>'
    spaces  = ' ' * (barLength - len(arrow))

    print('Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')

def check_duplicates(urls):
    new_urls = []
    for i in urls:
        if str(i) in new_urls:
            pass
        else:
            new_urls.append(i)
    return new_urls

def gen_driver():
    #A run avant de lancer
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
    return driver

def save_info (li, st):
    with open(f"results1/{st}.txt", "w") as f:
        for s in li:
            f.write(str(s) +"\n")

def open_info(li, st):
    with open(f"results1/{st}.txt", "r") as f:
        for line in f:
            li.append(str(line.strip()))

def tokenize(titles,descriptions, stopwords_list):
    lemonde_titles_complete = ""
    lemonde_descriptions_complete = ""
    lemonde_t_complete = []
    lemonde_d_complete = []
    lemonde_t = ""
    lemonde_d = ""

    stopwords_list.extend(["video","tres","contre","mois","propose","lo","veut","quots", "br","le","un","trois","quelles","mis","mise","non","depuis","autre","vient","selon","rapporte","quavec","les","vers","quelque","quelques","moins","grande","grandes","echospresidentielle","echoscovid","echosla","mis","cas","echos","comment","certains","certain","plusieurs","comment","pourquoi","cest","erreur","selection","quil","quelle","trop","encore","deja","loccasion","nest","nexclut","mag","fig","figarovox","figaro","ceux","sous","code","source","dune","dun","lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche","un","deux","trois","quatre","cinq","six","sept","huit","neuf","dix","sest","avoir","etre","apres","ans","a","va","l","c",'de', 'la','le', 'un', 'un', 'une','les','des','et','qui','que','pas','du','il','en','sur','emmanuel','macron', 'je','tu','elle','nous','vous','ils','elles','ce','ces','cette','mon','ton','son','janvier','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','decembre','fait','faire','faut','pour','dans','mais','ou','est','donc','or','ni','car','dont','dans','par','pour','quoi','ne','ce','se','avec','dit','sans','on','lui','aux','formes',"c'est",'lõ','cõest','nõst','quõil','nõest','comme','cet','meme','au','parce','sont','ont','si','memes','dõne','l','d','cela','ca','mesdames','messieurs','monsieur','madame','nos','notre','avons','devons','plus','aussi','crois','sommes','dire','alors','tant','doit','leur','train','sujet','tout','tous','pouvons','tous','entre', 'toute', 'ainsi', 'celui', "d'un", "d'une", "dõune", "j'ai", "n'est", "s'est", "quand", "ses", "deux", "n'avons", "quelque", "rendez", "n'y", "qu'il", "moi", "lõengagement", "titre", "chose", "l'avons", "d'autre", "ete", "part", "vois", "sa", "avait", "vos", "dis", "n'a", "celle", "d'abord", "leurs", "suis", "d'etre", "qu'elle", "qu'en", "fut"])

    for i in titles:
        lemonde_t += str(i).replace("0","").lower().replace("â","a").replace("à","a").replace("ç","c").replace("ê","e").replace("è","e").replace("é","e").replace("ë","e").replace("î","i").replace("ï","i").replace("ô","o").replace("û","u").replace("ù","u").replace("ü","u")\
                             .replace(".","").replace(",","").replace(":","").replace("c'","").replace("d'","").replace("l'","").replace("n'","").replace("t'","").replace("s'","").replace("j'","").replace("m'","").replace("-"," ").replace("(","").replace(")","").replace("«","").replace("»","").replace("’","").replace("les echos"," ").replace("echos"," ").replace("lesechos"," ").replace("lepoint", " ").replace("le point", " ").replace("le monde", " ")\
        .replace("lemonde", " ").replace("monde", " ").replace("point"," ").replace("valeurs actuelles"," ").replace("valeursactuelles"," ").replace("liberation"," ").replace("ocean","").replace("presse","").replace("http","").replace("https","").replace("ouest","").strip()
    lemonde_t = nltk.word_tokenize(lemonde_t)

    for i in descriptions:
        lemonde_d += str(i).replace("0","").lower().replace("â","a").replace("à","a").replace("ç","c").replace("ê","e").replace("è","e").replace("é","e").replace("ë","e").replace("î","i").replace("ï","i").replace("ô","o").replace("û","u").replace("ù","u").replace("ü","u")\
                             .replace("."," ").replace(","," ").replace(":"," ").replace("c'","").replace("d'","").replace("l'","").replace("n'","").replace("t'","").replace("s'","").replace("j'","").replace("m'","").replace("-"," ").replace("("," ").replace(")"," ").replace("«"," ").replace("»"," ").replace("’"," ").replace("les echos"," ").replace("echos"," ").replace("lesechos"," ").replace("lepoint", " ").replace("le point", " ").replace("le monde", " ")\
        .replace("lemonde", " ").replace("monde", " ").replace("point"," ").replace("valeurs actuelles"," ").replace("valeursactuelles"," ").replace("liberation"," ").replace("ocean","").replace("presse","").replace("http","").replace("https","").replace("ouest","").strip()
    lemonde_d = nltk.word_tokenize(lemonde_d)


    for i in lemonde_t:
        if str(i) not in stopwords_list:
            if i.isalpha():
                lemonde_t_complete.append(i)
                lemonde_titles_complete += f'{i} '

    for i in lemonde_d:
        if str(i) not in stopwords_list:
            if i.isalpha():
                lemonde_d_complete.append(i)
                lemonde_descriptions_complete += f'{i} '

    return lemonde_titles_complete, lemonde_descriptions_complete

def word_count(word_list):
    stopwords_list = stopwords.words('french')
    stopwords_list.extend(["video","tres","contre","mois","propose","lo","veut","quots", "br","le","un","trois","quelles","mis","mise","non","depuis","autre","vient","selon","rapporte","quavec","les","vers","quelque","quelques","moins","grand","grande","grandes","echosla","mis","cas","echos","comment","certains","certain","plusieurs","comment","pourquoi","cest","erreur","selection","quil","quelle","trop","encore","deja","loccasion","nest","nexclut","mag","fig","figarovox","figaro","ceux","sous","code","source","dune","dun","lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche","un","deux","trois","quatre","cinq","six","sept","huit","neuf","dix","sest","avoir","etre","apres","ans","a","va","l","c",'de', 'la','le', 'un', 'un', 'une','les','des','et','qui','que','pas','du','il','en','sur','emmanuel','macron', 'je','tu','elle','nous','vous','ils','elles','ce','ces','cette','mon','ton','son','janvier','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','decembre','fait','faire','faut','pour','dans','mais','ou','est','donc','or','ni','car','dont','dans','par','pour','quoi','ne','ce','se','avec','dit','sans','on','lui','aux','formes',"c'est",'lõ','cõest','nõst','quõil','nõest','comme','cet','meme','au','parce','sont','ont','si','memes','dõne','l','d','cela','ca','mesdames','messieurs','monsieur','madame','nos','notre','avons','devons','plus','aussi','crois','sommes','dire','alors','tant','doit','leur','train','sujet','tout','tous','pouvons','tous','entre', 'toute', 'ainsi', 'celui', "d'un", "d'une", "dõune", "j'ai", "n'est", "s'est", "quand", "ses", "deux", "n'avons", "quelque", "rendez", "n'y", "qu'il", "moi", "lõengagement", "titre", "chose", "l'avons", "d'autre", "ete", "part", "vois", "sa", "avait", "vos", "dis", "n'a", "celle", "d'abord", "leurs", "suis", "d'etre", "qu'elle", "qu'en", "fut"])
    counts = dict()
    a = ""
    #for i in word_list:
        #a += f'{i} '
    words = word_list.split()

    for word in words:
        if word not in stopwords_list:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    return counts

def wordcloud_titles(titles, save):
    wordcloud = WordCloud(width=2000,
                      height=2000,
                      prefer_horizontal=0.5,
                      background_color="rgba(255, 255, 255, 0)",
                      mode="RGBA").generate(titles)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    if save == 1:
        plt.savefig("wordcloud_titles.png")
    return plt.show

def wordcloud_descriptions(descriptions, save):
    wordcloud = WordCloud(width=2000,
                      height=2000,
                      prefer_horizontal=0.5,
                      background_color="rgba(255, 255, 255, 0)",
                      mode="RGBA").generate(descriptions)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    if save == 1:
        plt.savefig("wordcloud_titles.png")
    return plt.show

def color(values):
    if values in immigration:
        return "#E3A046"
    elif values in economie:
        return "#45B39D"
    elif values in securite:
        return "#E3E046"
    elif values in gouvernement:
        return "#85C1E9"
    elif values in vaccin:
        return "#BB8FCE"
    elif values in candidats:
        return "#FCAD22"
    else:
        return "#BDBCB9"
# Create a data frame with fake data
def treemap(number, titles_count):
    df = pd.DataFrame({'nb_people':list(titles_count.values())[:number], 'group':list(titles_count.keys())[:number]})
    df["color"] = df["group"].apply(color)

    # plot it
    plt.figure(figsize=(number/4,60))
    squarify.plot(sizes=df['nb_people'], pad=True,label=df['group'] ,color=df["color"], alpha=.8 ,text_kwargs={'fontsize':number/5})
    plt.axis('off')
    return plt.show()

def check_date(titles, descriptions, dates, min_date, max_date):
    min_date = pd.to_datetime(min_date, format="%d/%m/%Y")
    min_date = max(0,min_date.year-2021)*365+min_date.dayofyear+1
    max_date = pd.to_datetime(max_date, format="%d/%m/%Y")
    max_date = max(0,max_date.year-2021)*365+max_date.dayofyear+1
    new_titles = []
    new_descriptions = []
    new_dates = []
    for i in range(0,len(titles)):
        the_date = max(0,dates[i].year-2021)*365+dates[i].dayofyear+1
        if  the_date > min_date and the_date < max_date:
            new_titles.append(titles[i])
            new_descriptions.append(descriptions[i])
            new_dates.append(dates[i])
    return new_titles, new_descriptions, new_dates

def count_func(titles, descriptions):
    #titles = lesechos_titles
    #descriptions = lesechos_descriptions
    titles_complete, descriptions_complete = tokenize(titles,descriptions,stopwords.words('french'))
    titles_count = word_count(titles_complete)
    descriptions_count = word_count(descriptions_complete)
    return titles_count, descriptions_count

def day_word(dates, titles, descriptions, titles_count, descriptions_count):
    today = pd.to_datetime(datetime.today().strftime('%Y/%m/%d'), format="%Y/%m/%d")
    max_range = max(0,today.year-2021)*365+today.dayofyear+1
    d = {}
    for i in range(max_range):
        d['lesechosd_%s' % i] = []
        d['lesechost_%s' % i] = []
    for count,i in enumerate(dates):
        d[f'lesechost_{max(0,i.year-2021)*365+i.dayofyear}'].append(titles[count])
        d[f'lesechosd_{max(0,i.year-2021)*365+i.dayofyear}'].append(descriptions[count])
    e = {}
    lesechos_titles = pd.DataFrame.from_dict(titles_count, orient='index',columns=["Total"])
    lesechos_descriptions = pd.DataFrame.from_dict(descriptions_count, orient='index',columns=["Total"])
    for k in range (1,max_range):
        res = count_func(d[f'lesechost_{k}'], d[f'lesechosd_{k}'])
        e[f'lesechost_{k}'] = res[0]
        e[f'lesechosd_{k}'] = res[1]
        f = {}
        lesechos_titles[k] = 0
        lesechos_descriptions[k] = 0
        for j in titles_count.keys():
            try:
                f[j] = e[f'lesechost_{k}'][j]
            except KeyError:
                f[j] = 0
            lesechos_titles[k][j] = f[j]
        for j in descriptions_count.keys():
            try:
                f[j] = e[f'lesechosd_{k}'][j]
            except KeyError:
                f[j] = 0
            lesechos_descriptions[k][j] = f[j]
    return lesechos_titles, lesechos_descriptions

def topic_count(titles, descriptions, topic):
    count = 0
    words = []

    for i in titles.split():
        if i in topic:
            words.append(i)
            count += 1

    for i in descriptions.split():
        if i in topic:
            words.append(i)
            count += 1
    print(count)
    return words

def topic_count2(titles, descriptions, topic):
    count = 0
    words = []

    for i in titles.split():
        if i in topic:
            words.append(i)
            count += 1

    for i in descriptions.split():
        if i in topic:
            words.append(i)
            count += 1
    return count

def stuff_topics(titles, descriptions, topics):
    titles_complete, descriptions_complete = tokenize(titles,descriptions,stopwords.words('french'))
    listo = []
    for i in topics:
        i = topic_count2(titles_complete,descriptions_complete, i)
        listo.append(i)
    return listo

def stuff_candidates(titles, descriptions, candidates):
    titles_complete, descriptions_complete = tokenize(titles,descriptions,stopwords.words('french'))
    listo = []
    for i in candidates:
        i = topic_count2(titles_complete,descriptions_complete, i)
        listo.append(i)
    return listo

def get_viz_df(topics_count_pct):
    x = pd.DataFrame(topics_count_pct).transpose()
    x.columns = ["Normandie","Nord","Grand Est","Bourgogne","Auvergne","PACA","Occitanie","Ile de France","Aquitaine","Pays de la Loire","Bretagne","Centre Val de Loire"]
    x.index = ["immigration", "economie", "securite", "gouvernement", "vaccin", "candidats","delinquance",
        "environnement_cat_nat","environnement", "europe", "pouvoir_dachat","education","violence_aux_femmes","emploi",
          "retraite","industrie","mobilite_transport"]
    data = x
    data = data.transpose()
    data = data[['immigration', 'economie', 'securite', 'gouvernement',
       'candidats', 'delinquance', 'environnement_cat_nat', 'environnement',
       'europe', 'pouvoir_dachat', 'education', 'violence_aux_femmes',
       'emploi', 'retraite', 'industrie', 'mobilite_transport']]
    return data

def plot(data):
    fig = go.Figure()
    color_dict = {'immigration':"#808B96", 'economie':"#f6b26b","vaccin":"#f6b26b",'securite':"#ffff00", 'gouvernement':"#b4a7d6",
       'candidats':"#6aa84f", 'delinquance':"#e06666", 'environnement_cat_nat':"#6d9eeb", 'environnement':"#AED6F1",
       'europe':"#0000ff", 'pouvoir_dachat':"#cc0000", 'education':"#ff9900", 'violence_aux_femmes':"#6C3483 ",
       'emploi':"#1155cc", 'retraite':"#784212", 'industrie':"#ff00ff", 'mobilite_transport':"#38761d"}
    for i in data.columns:
        fig.add_trace(go.Bar(
        y=data[i],
        x=data.index,
        name=f"{i} %",
        marker=dict(
            color=color_dict[i],
            line=dict(color='rgba(0,128,0, 0.5)', width=0.05))))

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title="Région",

        yaxis=dict(
        title_text="Poids %",
        ticktext=["0%", "20%", "40%", "60%","80%","100%"],
        tickvals=[0, 20, 40, 60, 80, 100],
        tickmode="array",
        titlefont=dict(size=15),
        ),

        autosize=False,
        width=900,
        height=500,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title={
        'text': "Poids des Thèmes dans la Presse Quotidienne Régionale %",
        'y':0.85,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        barmode='stack')

    return fig

def get_viz_candidates(candidates, a_titles, a_descriptions):
    candidates_count = []
    for i in range(0,len(a_titles)):
        candidat = stuff_candidates(a_titles[i],a_descriptions[i], candidates)
        candidates_count.append(candidat)
    y = pd.DataFrame(candidates_count).transpose()
    y.columns = ["Normandie","Nord","Grand Est","Bourgogne","Auvergne","PACA","Occitanie","Ile de France","Aquitaine","Pays de la Loire","Bretagne","Centre Val de Loire"]
    y.index = ["zemmour","lepen","macron","pecresse","hidalgo","melenchon","jadot","autres"]
    y = y.reset_index()
    return y

def plot_candidates(y):
    fig = px.bar(y, x=y.columns, y=y["index"], orientation='h',
             height=600,
             width=800,
             title='')

    fig.update_layout(
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="green",
        xaxis_title="Nombre de Mentions",
        yaxis_title="Candidats",
        legend_title="Région",
        title={
        'text': "Mention des Candidats dans la Presse Quotidienne Régionale",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

    return fig
