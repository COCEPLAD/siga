import streamlit as st
import pandas as pd
import requests
import urllib

st.set_page_config('SIGA')

st.subheader('Generación de base completa del SIGA')

df = pd.read_excel('Estaciones.xlsx')

# Seleccionar la columna y transformarla en una lista
# estaciones = df['Id Interno'].tolist()

estaciones = ['A872872']

st.write(estaciones)

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
                st.write(df1)
                tabla = pd.concat([tabla, df1]) # concatenar df1 a tabla

        except:
            pass
        
        st.write(tabla)

        alert = st.container()
        
        st.download_button(
            label="Descargar",
            data=tabla.to_csv(decimal=',', sep=';', index=False).encode("utf-8"),
            file_name="base_estaciones.csv",
            mime="text/csv"
        )
    
    st.snow()
    alert.success('Descargá la base!:point_down:')
    









# def download_file(url):
#     local_filename = url.split("/")[-1]
#     with requests.get(url, stream=True) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192):
#                 f.write(chunk)
#     return local_filename

# if st.button('descarga'): 
#     download_file(url)

# soup = BeautifulSoup(response.content, "html.parser")

# codigos = []

# td_tags = soup.find_all("td", {"class": "ng-binding"})
# for tag in td_tags:
#     codigo = tag.text.strip()
#     codigos.append(codigo)

# st.write(codigos)
# # Realiza una solicitud HTTP a la página web
# response = requests.get(url_base)

# # Crea un objeto Beautiful Soup a partir del contenido HTML de la respuesta
# soup = BeautifulSoup(response.content, 'html.parser')

# st.write(response.content)

# # Encuentra todos los botones de descarga en el HTML utilizando su clase
# for boton in soup.find_all('button', {'class': 'btn-link', 'ng-click': 'download(e.idInterno)'}):
#     enlace_descarga = boton['ng-click'].split("'")[1]

#     st.write(boton)

# # Itera a través de los botones de descarga y descarga cada archivo Excel
# # for button in download_buttons:
# #     # Obtén la URL de descarga del archivo Excel haciendo clic en el botón
# #     url = url_base + button['ng-click'][12:-2]

# #     # Descarga el archivo Excel
# #     response = requests.get(url)

# #     # Escribe el contenido descargado en un archivo
# #     with open('file.xlsx', 'wb') as f:
# #         f.write(response.content)

# #     # Lee el archivo Excel en un DataFrame de pandas
# #     df = pd.read_excel('file.xlsx', sheet_name='Sheet1')
    
# #     # Realiza cualquier operación que necesites en el DataFrame
# #     # ...

# #     # Elimina el archivo descargado después de terminar de trabajar con él
# #     os.remove('file.xlsx')



    









# #
# # df_conj[["MOPK", "MIPK", "MAPK", "KG"]] = df_conj[["MOPK", "MIPK", "MAPK", "KG"]].astype(int)
# # df_conj = df_conj[df_conj['MIPK'] != 0]
# # df_conj['producto'] = df_conj['ESP'] + ' ' + df_conj['VAR']
# # df_tot = df_conj.groupby(by=['ESP', 'VAR', 'PROC', 'fecha', 'producto'], as_index=False).agg({'MOPK': 'mean'})
# # df_tot['MIPK'] = df_conj.groupby(by=['ESP', 'VAR', 'PROC', 'fecha', 'producto'], as_index=False).agg({'MIPK': 'min'})['MIPK']
# # df_tot['MAPK'] = df_conj.groupby(by=['ESP', 'VAR', 'PROC', 'fecha', 'producto'], as_index=False).agg({'MAPK': 'max'})['MAPK']
# # df_tot['Compra mínima'] = df_conj.groupby(by=['ESP', 'VAR', 'PROC', 'fecha', 'producto'], as_index=False).agg({'KG': 'min'})['KG']
# # df_tot['fecha'] = pd.to_datetime(df_tot['fecha']).dt.date
# # df_tot = df_tot.astype({"MOPK": int, "MIPK": int, "MAPK": int})
# #
# # ultima_fecha = df_conj["fecha"].max()
# # df_agg = df_tot.loc[df_tot["fecha"] == ultima_fecha]
# #
# # # CHECKEO DE NOVEDAD (EN FUNCIÓN DE LOS DÍAS PREVIOS DEL MES) Y AGREGADO DE LA COLUMNA:
# # df_sin_ultima = df_tot.loc[df_tot["fecha"] != ultima_fecha]
# # df_agg.loc[df_agg['producto'].isin(df_sin_ultima['producto']), 'NOVEDAD'] = 'False'
# # df_agg.loc[~df_agg['producto'].isin(df_sin_ultima['producto']), 'NOVEDAD'] = 'True'
# #
# # df_agg.rename(columns={'KG': 'Compra mínima'}, inplace=True)
# # df_agg = df_agg.fillna(0)
# # df_agg.sort_values(by='ESP', inplace=True)
# # df_agg.reset_index(inplace=True)
# #
# # ultima_fecha = df_agg["fecha"].max()
# # dia = ultima_fecha.day
# # ultima_fecha_dia = ultima_fecha.weekday()
# # dia_semana = semana[ultima_fecha_dia]
# # month = ultima_fecha.month
# # month = mes[month]
# #
# # st.markdown(f'''<h3 class='relevo'> Precios del {dia_semana} {dia} de {month} </h3>''', unsafe_allow_html=True)
# #
# # # AGREGA TABLA CON NOVEDADES SI LAS HAY:
# # if (df_agg['NOVEDAD'].str.contains('True').sum() > 0):
# #     st.markdown('''<h4> Novedades!! </h4>''', unsafe_allow_html=True)
# #     novedades = df_agg.loc[df_agg['NOVEDAD'] == 'True']
# #     novedades.rename(columns={'ESP': 'Especie', 'VAR': 'Variedad', 'MOPK': 'Precio por Kilo'}, inplace=True)
# #     novedades = novedades[['Especie', 'Variedad', 'Precio por Kilo']]
# #     novedades['Precio por Kilo'] = novedades['Precio por Kilo'].apply(lambda x: "$ {:.0f}".format(x))
# #     st.table(novedades)
#
#
# with st.expander('Buscar por letra'):
#     st.markdown(buscador, unsafe_allow_html=True)
#
# df_precios_previos = df_sin_ultima.groupby(by=['ESP', 'VAR', 'PROC'], as_index=False).mean()
#
# with st.form(key="add form2", clear_on_submit=False):
#
#     col1, col2 = st.columns([1,2])
#     submit = col1.container()
#     detall = st.container()
#     total = 0
#     detalle = ""
#
#     for index, row in df_agg.iterrows():
#
#         cultivo = row['ESP']
#         var = row['VAR']
#         proc = row['PROC']
#         precio = row['MOPK']
#         precio_min = row['MIPK']
#         precio_max = row['MAPK']
#         compra_min = row['Compra mínima']
#         culti = cultivo + ' ' + var + ' ' + proc
#         id = cultivo[:1]
#
#         #DETERMINACIÓN DE TENDENCIA EN FUNCIÓN DE SI EL PRECIOS ACTUAL ES 10% MAYOR O MENOR AL PROMEDIO DE LOS DÍAS PREVIOS:
#
#         indice = df_precios_previos.loc[(df_precios_previos['ESP'] == cultivo) & (df_precios_previos['VAR'] == var) & (
#                         df_precios_previos['PROC'] == proc), 'MOPK']
#
#         if indice.empty:
#             precio_previo = precio
#         else:
#             precio_previo = df_precios_previos.iloc[indice.index[0], df_precios_previos.columns.get_loc('MOPK')]
#
#         if precio_previo * 0.9 >= precio:
#             tendencia_graph = 'https://i.imgur.com/TYbum9Y.png'
#             tendencia_perc = ( precio_previo - precio ) / precio_previo
#             tendencia_perc = "{:.0%}".format(tendencia_perc)
#             text = f'<p id="var_negat" class="card-text"> {tendencia_perc} </p></div>'
#         elif precio_previo * 1.1 <= precio:
#             tendencia_graph = 'https://i.imgur.com/LCiBOFI.png'
#             tendencia_perc = (precio - precio_previo) / precio_previo
#             tendencia_perc = "{:.0%}".format(tendencia_perc)
#             text = f'<p id="var_posit" class="card-text"> {tendencia_perc} </p></div>'
#         else:
#             tendencia_graph = None
#             text = None
#
#         #FUNCION QUE CREA LA CARD:
#         st.markdown(card2(id, culti, precio, precio_min, precio_max, tendencia_graph, text, compra_min, verdus_img.get(cultivo, 'https://i.imgur.com/sW0bxrG.png')), unsafe_allow_html=True)
#
#         cantidad = st.number_input("Cantidad (Kg)", key=row, min_value=0, value=0, step=compra_min)
#
#         total = total + (cantidad * precio)
#
#         if cantidad != 0:
#             cant_str = str(cantidad)
#             prec_str = str(precio)
#             detalle_unit = f' {cant_str} kg de {culti} x ${prec_str}'
#
#         else:
#             cultivo = ""
#             precio = ""
#             detalle_unit = ""
#
#         detalle = f'{detalle}  \n {detalle_unit}\n'
#
#     if submit.form_submit_button('Calcular compra'):
#         total = int(round(total))
#
#         if total != 0:
#             detall.markdown(f'''<h3 class='relevo'> Total: ${total} </h3>''', unsafe_allow_html=True)
#             detall.success(f'Detalle:\n {detalle}\n')
#         else:
#             detall.info('Para estimar una compra ingresa las cantidades para cada producto')
#
