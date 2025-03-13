import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Formação", layout="wide")

st.logo("images/logo.png", size="large")

st.sidebar.markdown("Desenvolvido por Edson Leonardo ®️ 2025")
col1, col2 = st.sidebar.columns([0.5, 0.5])
col1.markdown("""<a href="https://github.com/EdLeo0708"><img src="https://cdn3.emoji.gg/emojis/6705-githubblack.png" width="64px" height="64px" alt="github"></a>""", unsafe_allow_html=True)
col2.markdown("""<a href="https://www.linkedin.com/in/edson-leonardo-4b500a289/"><img src="https://cdn3.emoji.gg/emojis/70322-linkedin.png" width="64px" height="64px" alt="LinkedIn"></a>""""", unsafe_allow_html=True)

st.image("images/formações.png", width=150)
st.title("Formação")

st.header("Engenharia de Software- FIAP")
st.markdown("Agosto de 2023 - Julho de 2027, SP")
st.write("A Engenharia de Software é uma área da computação focada no desenvolvimento, manutenção e gerenciamento de sistemas e aplicações. Ela envolve a aplicação de princípios científicos e boas práticas para ")
st.write("garantir que o software seja confiável, eficiente, seguro e escalável. O curso abrange desde a programação e design de sistemas até metodologias ágeis, testes, segurança e DevOps, proporcionando uma formação")
st.write("completa para atuar no desenvolvimento de soluções tecnológicas inovadoras.")