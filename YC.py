import streamlit as st
import pandas as pd
import numpy as np
import codecs as cd
import plotly.express as px

st.set_page_config(page_title="Canales de YouTube con más suscriptores",
                   page_icon="YL.png")
st.image("banner.jpg")

DATE_COLUMN = 'started_at'
name_link =cd.open('YC.csv')

st.title('Los canales de YouTube con más suscriptores')
st.header('Autor: Aldo Torres Ramírez')
st.header('Matrícula: zS20006781')

st.sidebar.image("Logo.jpg")
st.sidebar.markdown("##")
sidebar= st.sidebar

@st.cache_data
def load_data(nrows):
    name_link = cd.open('YC.csv',)
    data = pd.read_csv(name_link, nrows=nrows)
    return data

def filtro_youtuber(Youtuber):
    canal_filt = data[data['Youtuber'].str.upper().str.contains(Youtuber)]
    return canal_filt

data_load_state = st.text('Cargando datos...')
data= load_data(1000)
data_load_state.text('Datos cargados')

agree=sidebar.checkbox("Mostrar todos los canales")
if agree:
    st.header("Todos los canales")
    st.dataframe(data)
    
nombreCanal = st.sidebar.text_input('Nombre del canal:')
botonBuscar = st.sidebar.button('Buscar canal')

if (botonBuscar):
   canales = filtro_youtuber(nombreCanal.upper())
   count_row = canales.shape[0]
   st.header("Canales")
   st.write(f"Total de canales mostrados: {count_row}")
   st.write(canales)

agreeHistogram=sidebar.checkbox("Mostrar histograma")
fig_subscribers = px.histogram(data,
                   x="subscribers",
                   title="Numero de suscriptores por canal",
                   labels=dict(Episodes="Numero de suscriptores por canal"),
                   color_discrete_sequence=["#634a71"],
                   template="plotly_white"
                   )
fig_subscribers.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.header("Histograma de suscriptores")
st.plotly_chart(fig_subscribers)
st.write("Se muestra el número de canales que tienen determinada cantidad de suscriptores")

agreeBar=sidebar.checkbox("Mostrar gráfica de barras")
videocountBytitle=(
    data.groupby(by=['started']).count()
    )
fig_vc=px.bar(videocountBytitle,
                x=videocountBytitle.index,
                y='Youtuber',
                title="Cantidad de youtubers que iniciaron en cada año",
                labels=dict(Title="Años de inicio de cada youtuber",Source="started",),
                color_discrete_sequence=["#f86749"],
                template="plotly_white")
fig_vc.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.header("Gráfica de barras")
st.plotly_chart(fig_vc)
st.write("Se muestra la cantidad de youtubers que inició por cada año")

agreeScatter=sidebar.checkbox("Mostrar gráfica de scatter")
if agreeScatter:
    category=data['category']
    youtuber=data['Youtuber']
    fig_scatter=px.scatter(data,
                             x=youtuber,
                             y=category,
                             labels=dict(category='Categoria',youtuber="youtuber"),
                             title="Categoria de cada canal",
                             template="plotly_white")
    fig_scatter.update_layout(plot_bgcolor="rgba(0,0,0,0)")
    st.header("Gráfica de Scatter")
    st.plotly_chart(fig_scatter)
    st.write("Se muestra la categoría de cada canal")
    
#Se espera agregar más funcionalidades