
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
st.markdown("<h1 style='text-align: center; color: black;'Analyse PQR</h1>", unsafe_allow_html=True)

y = pd.read_csv("y.csv", index_col=0)
x = pd.read_csv("x.csv",index_col=0)

y = y.reset_index()

APP_NAME = "Analyse PQR"
st.markdown("<h1 style='text-align: center; color: black;'Analyse PQR</h1>", unsafe_allow_html=True)

st.write(plot(x))
st.write(plot_candidates(y))