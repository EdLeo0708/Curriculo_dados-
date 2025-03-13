import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Skills", layout="wide")

st.logo("images/logo.png", size="large")

st.sidebar.markdown("Desenvolvido por Edson Leonardo ®️ 2025")
col1, col2 = st.sidebar.columns([0.5, 0.5])
col1.markdown("""<a href="https://github.com/EdLeo0708"><img src="https://cdn3.emoji.gg/emojis/6705-githubblack.png" width="64px" height="64px" alt="github"></a>""", unsafe_allow_html=True)
col2.markdown("""<a href="https://www.linkedin.com/in/edson-leonardo-4b500a289/"><img src="https://cdn3.emoji.gg/emojis/70322-linkedin.png" width="64px" height="64px" alt="LinkedIn"></a>""""", unsafe_allow_html=True)

st.image("images/certificados.png", width=150)
st.title("Certificados")

df = pd.DataFrame(pd.read_csv("databases/Certificados.csv"))

st.table(df)