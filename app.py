# importar librerías necesarias
import streamlit as st
import pandas as pd
import plotly_express as px

# -------------------------------------------------CARGA DE ARCHIVOS---------------------------------------------------
# crear el dataframe con los datos del archivo csv
file_path = 'vehicles_us.csv'
df_vehicles = pd.read_csv(file_path)

# -------------------------------------------DISEÑO DE LA APLICACIÓN WEB---------------------------------------------
# insertar un encabezado para la aplicación web
st.header('Crea visualizaciones gráficas de diferentes tipos con los datos de anuncios de venta de vehículos en Estados Unidos',)

# # # HISTOGRAMA # # #
# insertar titulo de histograma
st.write('## Crea un histograma')

# lista con las columnas posibles para graficar un histograma
hist_options = ['price','odometer','model_year','cylinders','type','paint_color']

# crea una caja para seleccionar una columna para graficar un histograma
hist_selection = st.selectbox('Selecciona una categoría para graficar el histograma',
                              hist_options,
                              placeholder='Escoge una opción',
                              index=0)

# crea un botón para construir un histograma con la opción elegida
hist_button = st.button('Construir histograma')
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write(f'Histograma de {hist_selection} para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(df_vehicles, x=hist_selection)
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True) 

# # # GRÁFICO DE DISPERSIÓN # # #
# insertar titulo de grafico de dispersión
st.write('## Crea un gráfico de dispersión')
# lista con las columnas posibles para el eje x del grafico de dispersión
scatter_options_x = ['odometer','model_year','days_listed','paint_color']

# crea una caja para seleccionar una columna para el eje x del gráfico de dispersión
scatter_selection = st.selectbox('Selecciona una categoría para graficar contra el precio',
                              scatter_options_x,
                              placeholder='Escoge una opción',
                              index=0)            

# crea casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')
if build_scatter: #al hacer click en la casilla
        st.write(f'Gráfico de dispersión del precio de vehículos y {scatter_selection}')

        # crear un gráfico de dispersión
        fig_2 = px.scatter(df_vehicles, x=scatter_selection, y='price')

        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig_2, use_container_width=True)