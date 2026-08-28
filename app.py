import pandas as pd
import plotly.express as px
import streamlit as st


car_data = pd.read_csv('vehicles_us.csv')


st.header('Análisis de anuncios de vehículos')

hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Distribución del millaje de los vehículos')

    fig = px.histogram(
        car_data,
        x='odometer',
        title='Distribución del millaje'
    )

    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Relación entre millaje y precio')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Relación entre millaje y precio'
    )

    st.plotly_chart(fig, use_container_width=True)

