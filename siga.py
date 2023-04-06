import streamlit as st
import pandas as pd
import requests
import urllib

st.set_page_config('SIGA')

st.subheader('Generación de base completa del SIGA')

# df = pd.read_excel('Estaciones.xlsx')

# # Seleccionar la columna y transformarla en una lista
# estaciones = df['Id Interno'].tolist()

estaciones = ['A872872']

if st.button('Crear base SIGA'):

    with st.spinner('Armando base completa SIGA :rain_cloud::mostly_sunny: Esta operación puede tardar unos minutos'):

        tabla = pd.DataFrame(columns=[
    "id_estacion",
    "Fecha",
    "Temperatura_Abrigo_150cm",
    "Temperatura_Abrigo_150cm_Maxima",
    "Temperatura_Abrigo_150cm_Minima",
    "Temperatura_Intemperie_5cm_Minima",
    "Temperatura_Intemperie_50cm_Minima",
    "Temperatura_Suelo_5cm_Media",
    "Temperatura_Suelo_10cm_Media",
    "Temperatura_Inte_5cm",
    "Temperatura_Intemperie_150cm_Minima",
    "Humedad_Suelo",
    "Precipitacion_Pluviometrica",
    "Precipitacion_Cronologica",
    "Precipitacion_Maxima_30minutos",
    "Heliofania_Efectiva",
    "Heliofania_Relativa",
    "Tesion_Vapor_Media",
    "Humedad_Media",
    "Humedad_Media_8_14_20",
    "Rocio_Medio",
    "Duracion_Follaje_Mojado",
    "Velocidad_Viento_200cm_Media",
    "Direccion_Viento_200cm",
    "Velocidad_Viento_1000cm_Media",
    "Direccion_Viento_1000cm",
    "Velocidad_Viento_Maxima",
    "Presion_Media",
    "Radiacion_Global",
    "Horas_Frio",
    "Unidades_Frio"
    ])

        try:

            for estacion in estaciones:

                url = f"http://siga.inta.gob.ar/document/series/{estacion}.xls"
                
                st.write(url)

                        # Descarga de archivo Excel
                def download_excel_file(url):
                    with urllib.request.urlopen(url) as response:
                        data = response.read()
                    return data

                file = download_excel_file(url)

                # Carga de archivo Excel en tabla de Pandas
                def load_excel_to_df(file):
                    df = pd.read_excel(file, engine='xlrd')
                    df.insert(0, 'id_estacion', estacion)
                    return df

                df1 = load_excel_to_df(file)
                tabla = pd.concat([tabla, df1]) # concatenar df1 a tabla

        except:
            pass

        alert = st.container()
        
        st.download_button(
            label="Descargar",
            data=tabla.to_csv(decimal=',', sep=';', index=False).encode("utf-8"),
            file_name="base_estaciones.csv",
            mime="text/csv"
        )
    
    st.snow()
    alert.success('Descargá la base!:point_down:')
    
