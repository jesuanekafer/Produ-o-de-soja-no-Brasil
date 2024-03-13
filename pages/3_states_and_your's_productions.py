import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(
    page_title="Produção de Soja no Brasil", 
    page_icon="🏠", 
    layout="wide"
    )

st.title("🌿 Produção de Soja no Brasil")

dataFrame = pd.read_csv("datasets/trase_brazil_soy_data.csv")

# Agrupar os dados por 'STATE' e contar o número de registros/vendas para cada estado
data_aggregated = dataFrame.groupby('STATE').size().reset_index(name='count')

# Dados geograficos por estado (precisa ter o mesmo nome que está no csv pra conseguir mapear)
estados_brasil_data = {
    'STATE': [
        'ACRE', 'ALAGOAS', 'AMAPA', 'AMAZONAS', 'BAHIA', 'CEARA', 'DISTRITO FEDERAL', 'GOIAS', 
        'MARANHAO', 'MATO GROSSO', 'MATO GROSSO DO SUL', 'MINAS GERAIS', 'PARA', 'PARAIBA', 'PARANA', 
        'PIAUI', 'RIO GRANDE DO SUL', 'RONDONIA', 'RORAIMA', 'SANTA CATARINA', 'SAO PAULO', 'TOCANTINS'
    ],
    'lat': [
        -9.02, -9.57, 2.05, -3.47, -12.97, -5.20, -15.83, -19.19, -15.93, 
        -4.90, -12.64, -20.51, -18.10, -3.79, -7.12, -5.81, -30.17, -11.22, 1.89, -27.33, -22.19, -10.25
    ],
    'lon': [
        -70.55, -36.82, -52.00, -64.80, -41.81, -39.30, -47.86, -40.34, -50.14, 
        -45.30, -55.42, -54.54, -44.38, -52.48, -36.95, -36.82, -53.78, -63.58, -61.22, -51.22, -46.64, -48.33
    ],
}

estados_brasil = pd.DataFrame(estados_brasil_data)

# mescla os arrays para adicionar longitude a latitude nas somas dos estados
dados_completos = pd.merge(estados_brasil, data_aggregated, on='STATE', how='left')

# Criar o mapa
view = pdk.ViewState(
    latitude=-14.2350, 
    longitude=-51.9253,
    zoom=3,
    pitch=500,
    min_zoom=2, 
    max_zoom=15)
layers = [
    pdk.Layer(
    "ColumnLayer",
    data=dados_completos,
    get_position=["lon", "lat"],
    get_elevation="count",
    elevation_scale=10,
    radius=100000,
    get_fill_color="[255, 165, 0, 255]",  # lalanja
    pickable=True,
    auto_highlight=True,
)
]
# Mostrar o mapa no Streamlit
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/navigation-night-v1",
    initial_view_state=view,
    layers=layers
))