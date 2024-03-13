import streamlit as st

dataFrame = st.session_state['data']

st.set_page_config(
    page_title="Index",
    page_icon="🎲",
    layout="wide"
)

st.title("🌿 Produção de Soja no Brasil")

# Printando tabela
st.write(dataFrame)