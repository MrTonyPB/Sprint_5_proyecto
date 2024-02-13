import streamlit as st
import pandas as pd
import plotly_express as px

file_path = 'vehicles_us.csv'
df_vehicles = pd.read_csv(file_path)

st.header('Vehículos')

hist_button = st.button('Construir histograma')
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(df_vehicles, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True) 