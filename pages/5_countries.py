import streamlit as st
import altair as alt

dataFrame = st.session_state['data']

# Definindo a configuração da página
st.set_page_config(
    page_title="Gráficos",
    page_icon="📈",
    layout="wide"
)

st.title("Importações dos países") 

# Agrupando os dados por estado e ano e somando as vendas
vendas_por_pais_ano = dataFrame.groupby(['COUNTRY OF FIRST IMPORT', 'YEAR']).size().reset_index(name='count')

# Renomeando as colunas para corresponder à estrutura do gráfico
vendas_por_pais_ano.rename(columns={"pais": 'COUNTRY OF FIRST IMPORT', "ano": 'YEAR', "col3": 'FOB_USD'}, inplace=True)

# Criando o gráfico de barras com Altair
chart = alt.Chart(vendas_por_pais_ano).mark_bar().encode(
    x='YEAR:O',  # Definindo o eixo x como ano (ordinal)
    y='count:Q',  # Definindo o eixo y como quantidade vendida (quantitativo)
    color=alt.Color('COUNTRY OF FIRST IMPORT:N', legend=None),  # Colorindo as barras por estado, sem legenda
    tooltip=['COUNTRY OF FIRST IMPORT', 'YEAR', 'count']  # Adicionando tooltips com informações adicionais
).properties(
    width=800,  # Definindo a largura do gráfico
    height=400  # Definindo a altura do gráfico
).configure_axis(
    labelFontSize=12,  # Tamanho da fonte dos rótulos dos eixos
    titleFontSize=14  # Tamanho da fonte dos títulos dos eixos
).configure_title(
    fontSize=18  # Tamanho da fonte do título do gráfico
)

# Exibindo o gráfico
st.altair_chart(chart, use_container_width=True)
