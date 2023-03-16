import streamlit as st
import pandas as pd
import numpy as np
import codecs
import plotly.express as px

st.set_page_config(page_title="YouTube channels list",
                   page_icon="YL.png")
st.image("banner.jpg")

DATE_COLUMN = 'started_at'
name_link =codecs.open('YC.csv')

st.title('Most Subscribed YouTube Channels')
st.header('Aldo Torres Ramírez')
st.header('zS20006781')

st.sidebar.image("Logo.jpg")
st.sidebar.markdown("##")
sidebar= st.sidebar

@st.cache
def load_data(nrows):
    name_link = codecs.open('YC.csv',)
    data = pd.read_csv(name_link, nrows=nrows)
    return data

def filtro_canal(channel):
    channel_filt = data[data['Name'].str.upper().str.contains(channel)]
    return channel_filt

def filtro_youtuber(youtuber):
    youtuber_filt = data[data['YouTuber'] == youtuber]
    return youtuber_filt

data_load_state = st.text('Loading data...')
data= load_data(1000)
data_load_state.text('Loading data...done!')

agree=sidebar.checkbox("Mostrar todos los canales")
if agree:
    st.header("Todos los canales")
    st.dataframe(data)
    
tituloCanal = st.sidebar.text_input('Titulo del canal:')
botonBuscar = st.sidebar.button('Buscar canal')

if (botonBuscar):
   canal = filtro_canal(tituloCanal.upper())
   count_row = canal.shape[0]
   st.header("Canales")
   st.write(f"Total de canales mostrados: {count_row}")
   st.write(canal)
   
agreeHistogram=sidebar.checkbox("Mostrar histograma")
if agreeHistogram:
    fig_volumes = px.histogram(data,
                       x="volumes",
                       title="Numero de suscriptores por canal",
                       color_discrete_sequence=["#634a71"],
                       template="plotly_white"
                       )
    fig_volumes.update_layout(xaxis_title='Suscriptores',yaxis_title='Numero de suscriptores')
    fig_volumes.update_layout(plot_bgcolor="rgba(0,0,0,0)")
    st.header("Histograma de suscriptores")
    st.plotly_chart(fig_volumes)
    st.write("Se muestra el numero de suscriptores por canal")   
    
agreeBar=sidebar.checkbox("Mostrar gráfica de barras")
if agreeBar:
    scoredBytype=(
        data.groupby(by=['type']).sum()['scored_by']
        )
    fig_type=px.bar(scoredBytype,
                    x=scoredBytype.index,
                    y="scored_by",
                    title="a",
                    color_discrete_sequence=["#f86749"],
                    template="plotly_white")
    fig_type.update_layout(xaxis_title='Categoria',yaxis_title='a')
    fig_type.update_layout(plot_bgcolor="rgba(0,0,0,0)")
    st.header("Grafica de barras")
    st.plotly_chart(fig_type)
    st.write("Se muestra la cantidad de suscriptores por canal")

agreeScatter=sidebar.checkbox("Mostrar gráfica scatter")
if agreeScatter:
    volumes=data['Suscriptores']
    tipe=data['type']
    fig_scatter=px.scatter(data,
                             x=volumes,
                             color=tipe,
                             labels=dict(volumes='Numero de volumenes',chapters="Capitulos", type="Categoria"),
                             title="Capitulos por cantidad de volumenes",
                             template="plotly_white")
    fig_scatter.update_layout(plot_bgcolor="rgba(0,0,0,0)")
    st.header("Grafica de Scatter")
    st.plotly_chart(fig_scatter)
    st.write("a")
