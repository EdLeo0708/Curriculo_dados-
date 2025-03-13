import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import statistics as sta
import os

def variancia(media, dados):
    return sum((x - media) ** 2 for x in dados) / len(dados)

st.set_page_config(page_title="Análise de IoT no Brasil", layout="wide")

st.logo("images/logo.png", size="large")

st.sidebar.markdown("Desenvolvido por Edson Leonardo ®️ 2025")
col1, col2 = st.sidebar.columns([0.5, 0.5])
col1.markdown("""<a href="https://github.com/EdLeo0708"><img src="https://cdn3.emoji.gg/emojis/6705-githubblack.png" width="64px" height="64px" alt="github"></a>""", unsafe_allow_html=True)
col2.markdown("""<a href="https://www.linkedin.com/in/edson-leonardo-4b500a289/"><img src="https://cdn3.emoji.gg/emojis/70322-linkedin.png" width="64px" height="64px" alt="LinkedIn"></a>""""", unsafe_allow_html=True)

st.title("Análise de Dados sobre IoT no Brasil")

st.write(
    "A Internet das Coisas (IoT) tem sido amplamente adotada por empresas brasileiras, "
    "proporcionando eficiência operacional e novos modelos de negócio. O conjunto de dados "
    "analisado baseia-se em informações do site [Brasil, País Digital](https://brasilpaisdigital.com.br/internet-das-coisas-nas-empresas-brasileiras-alguns-dados-e-dois-alertas/) "
    "sobre a implementação de IoT no Brasil."
)

# Definição das perguntas de análise
st.subheader("Principais Perguntas de Análise")
st.markdown("""
- Quais setores mais adotam IoT?
- Qual a variação da adoção de IoT entre setores?
- A adoção de IoT segue uma distribuição estatística específica?
- Existe correlação entre a taxa de adoção de IoT e outros fatores analisados?
""")

# Definindo o diretório dos arquivos CSV
data_dir = "databases"

# Verificando se os arquivos CSV existem
files = [f for f in os.listdir(data_dir) if f.endswith(".csv") and "Certificados" not in f]

if not files:
    st.error("❌ Nenhum arquivo de dados encontrado na pasta 'databases'. Verifique se os arquivos .csv estão no diretório correto.")
    st.stop()

# Dicionário de possíveis renomeações
colunas_renomeadas = {
    "Porte da Empresa": "Setor",
    "Aplicação de IoT": "Setor",
    "País": "Setor",
    "Percentual de Adoção de IoT (%)": "Adoção (%)",
    "Percentual de Uso (%)": "Adoção (%)"
}

# Carregar arquivos CSV e verificar colunas
dfs = []

for file in files:
    file_path = os.path.join(data_dir, file)
    df = pd.read_csv(file_path)

    # Renomeia colunas conforme necessário
    df.rename(columns=colunas_renomeadas, inplace=True)

    # Verificar se a coluna "Adoção (%)" existe após renomeação
    if "Adoção (%)" in df.columns:
        dfs.append(df)

# Se nenhum DataFrame válido foi carregado, interrompe a execução
if not dfs:
    st.error("❌ Nenhum arquivo contém as colunas esperadas. Verifique os arquivos CSV.")
    st.stop()

# Concatenar os DataFrames
dados_iot = pd.concat(dfs, ignore_index=True)

st.success("✅ Todos os arquivos foram carregados corretamente!")

# Identificação dos tipos de variáveis
st.subheader("Tipos de Variáveis no Conjunto de Dados")
st.write("""
- **Setor (Categórica Nominal)**: Representa os diferentes setores das empresas analisadas.
- **Adoção (%) (Numérica Contínua)**: Percentual de empresas que adotaram IoT em cada setor.
""")

pages = st.selectbox("Selecione a análise:", [
    "Taxa de Adoção de IoT",
    "Setores que mais utilizam IoT",
    "Modelagem Estatística"
])

if pages == "Taxa de Adoção de IoT":
    st.header("Taxa de Adoção de IoT nas Empresas Brasileiras")

    media_iot = round(dados_iot["Adoção (%)"].mean(), 2)
    mediana_iot = round(dados_iot["Adoção (%)"].median(), 2)
    moda_iot = round(sta.mode(dados_iot["Adoção (%)"]))
    desvio_iot = round(np.std(dados_iot["Adoção (%)"]), 2)
    variancia_iot = variancia(media_iot, dados_iot["Adoção (%)"])

    st.subheader("Medidas Estatísticas")
    st.write(f"Média: {media_iot}%")
    st.write(f"Mediana: {mediana_iot}%")
    st.write(f"Moda: {moda_iot}%")
    st.write(f"Desvio Padrão: {desvio_iot}%")
    st.write(f"Variância: {variancia_iot}%")

    fig = go.Figure()
    fig.add_trace(go.Bar(x=dados_iot["Setor"], y=dados_iot["Adoção (%)"], name="Taxa de Adoção"))
    fig.update_layout(title="Taxa de Adoção de IoT por Setor", xaxis_title="Setor", yaxis_title="Adoção (%)")
    st.plotly_chart(fig)

    # Análise de correlação
    st.subheader("Correlação entre Variáveis")
    correlacao = dados_iot.corr(numeric_only=True)
    st.write("Matriz de Correlação:")
    st.write(correlacao)

elif pages == "Setores que mais utilizam IoT":
    st.header("Setores que Mais Utilizam IoT")

    fig = px.pie(dados_iot, names="Setor", values="Adoção (%)", title="Distribuição da Adoção de IoT por Setor")
    st.plotly_chart(fig)

elif pages == "Modelagem Estatística":
    st.header("Modelagem Estatística para IoT")

    # Justificativa das distribuições
    st.subheader("Justificativa para as Distribuições Escolhidas")
    st.write("""
    - **Distribuição Binomial**: É usada porque a adoção de IoT pode ser considerada um evento binário, onde uma empresa adota ou não adota a tecnologia.
    - **Distribuição de Poisson**: Foi escolhida para modelar a frequência com que novas empresas adotam IoT, considerando uma taxa média de adoção por período.
    """)

    st.subheader("Distribuição Binomial")
    n = 10  # Número de empresas analisadas
    p = dados_iot["Adoção (%)"].mean() / 100  # Probabilidade de adoção de IoT

    x = np.arange(0, n + 1)
    y = stats.binom.pmf(x, n, p)

    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title="Distribuição Binomial para Adoção de IoT", xaxis_title="Número de Empresas", yaxis_title="Probabilidade")
    st.plotly_chart(fig)

    st.subheader("Distribuição de Poisson")
    lambda_iot = round(dados_iot["Adoção (%)"].mean() / 10, 2)  # Média ajustada
    x = np.arange(0, 15)
    y = stats.poisson.pmf(x, lambda_iot)

    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title="Distribuição de Poisson - Novas Empresas Adotando IoT", xaxis_title="Número de Empresas", yaxis_title="Probabilidade")
    st.plotly_chart(fig)

st.markdown("### Referências:")
st.write("[Brasil, País Digital - Implementação de IoT no Brasil](https://brasilpaisdigital.com.br/internet-das-coisas-nas-empresas-brasileiras-alguns-dados-e-dois-alertas/)")
