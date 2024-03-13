import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

if 'data' not in st.session_state:
    dataFrame = pd.read_csv("datasets/trase_brazil_soy_data.csv", index_col=0)
    st.session_state['data'] = dataFrame

fonte = "Kode Mono"

st.title("🌿 Produção de Soja no Brasil")

# Usando HTML para definir a fonte para o texto
st.markdown(f'<p style="font-family:{fonte}">A produção de soja no Brasil desempenha um papel significativo tanto na economia do país quanto na busca por práticas agrícolas sustentáveis. O Brasil é um dos principais produtores mundiais de soja, e sua produção tem contribuído de maneira substancial para o crescimento econômico e o desenvolvimento rural.</p>', unsafe_allow_html=True)

st.markdown(f'<p style="font-family:{fonte}">A soja brasileira não apenas gera receita por meio das exportações, impulsionando a balança comercial do país, mas também cria empregos ao longo de toda a cadeia produtiva, desde o plantio e colheita até o processamento e transporte. Além disso, a produção de soja contribui para o desenvolvimento de infraestrutura em regiões agrícolas, incentivando investimentos em estradas, portos e armazéns.</p>', unsafe_allow_html=True)

st.markdown(f'<p style="font-family:{fonte}">Além dos benefícios econômicos, a produção de soja no Brasil também tem avançado em direção à sustentabilidade. Muitos produtores adotaram práticas agrícolas sustentáveis, como o plantio direto, que reduz a erosão do solo e o uso de agrotóxicos, e o sistema de integração lavoura-pecuária-floresta, que promove a diversificação e a conservação dos recursos naturais.</p>', unsafe_allow_html=True)

st.markdown(f'<p style="font-family:{fonte}">Esses esforços visam não apenas aumentar a produtividade e a rentabilidade das fazendas, mas também mitigar os impactos negativos da agricultura no meio ambiente. A produção de soja sustentável no Brasil visa equilibrar a expansão agrícola com a conservação dos ecossistemas naturais, a proteção da biodiversidade e a redução das emissões de gases de efeito estufa.</p>', unsafe_allow_html=True)

st.markdown(f'<p style="font-family:{fonte}">Esta página foi criada para fornecer acesso a informações relevantes sobre a produção de soja. Aqui, você pode encontrar dados atualizados, análises que abordam diversos aspectos da produção de soja no Brasil, desde sua importância econômica até suas implicações ambientais e sociais. Seja você um produtor rural, um estudante, um pesquisador ou um interessado em aprender mais sobre agricultura sustentável, esperamos que este espaço seja útil para expandir seu conhecimento e promover discussões construtivas sobre o futuro do agronegócio brasileiro.</p>', unsafe_allow_html=True)

