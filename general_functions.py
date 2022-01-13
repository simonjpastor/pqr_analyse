import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go


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
        legend_title="Thèmes",
        xaxis_title="Région",

        yaxis=dict(
        title_text="Poids %",
        ticktext=["0%", "20%", "40%", "60%","80%","100%"],
        tickvals=[0, 20, 40, 60, 80, 100],
        tickmode="array",
        titlefont=dict(size=15),
        ),

        autosize=False,
        width=1000,
        height=600,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title={
        'text': "Poids des Thèmes dans la Presse Quotidienne Régionale % (hors covid et vaccin)",
        'y':0.85,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        barmode='stack')

    return fig


def plot_candidates(data):
    data = data.reset_index()
    fig = px.bar(data, x=data.columns, y=data["index"], orientation='h',
             #height=600,
             #width=800,
             )

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

def plot_all(data):
    #data = data.reset_index
    data = data.transpose()
    data = data[['immigration', 'economie', 'securite', 'gouvernement',
       'candidats', 'delinquance', 'environnement_cat_nat', 'environnement',
       'europe', 'pouvoir_dachat', 'education', 'violence_aux_femmes',
       'emploi', 'retraite', 'industrie', 'mobilite_transport']]
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
        yaxis=dict(
        title_text="Poids %",
        ticktext=["0%", "20%", "40%", "60%","80%","100%"],
        tickvals=[0, 20, 40, 60, 80, 100],
        tickmode="array",
        titlefont=dict(size=15),
        legend_tile="Thèmes",
    ),
    autosize=False,
    #width=1200,
    #height=500,
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
