import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Analises de dados de veículos nos EUA')  # título

car_data = pd.read_csv('vehicles_us.csv')  # lendo os dados
build_histogram = st.checkbox('Criar um histograma')  # criar um botão
build_scatter = st.checkbox('Criar um grafico de dispersao')  # criar um botão

if build_histogram:
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer",
                       color_discrete_sequence=['green'])
    fig.update_layout(
        width=1200,  # Largura em pixels
        height=600   # Altura em pixels
    )

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para preço de carros por milhas rodadas')

    # criar um gráfico de dispersão
    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price",
                     color_discrete_sequence=['black'])
    fig.update_layout(
        width=1200,  # Largura em pixels
        height=600   # Altura em pixels
    )
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
