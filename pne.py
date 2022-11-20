#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import json
import requests
import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title="Projeto Final", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# GIFS
lottie_database = load_lottieurl(
    "https://assets6.lottiefiles.com/packages/lf20_qp1q7mct.json"
)
lottie_exploracao = load_lottieurl(
    "https://assets1.lottiefiles.com/packages/lf20_bdlrkrqv.json"
)
lottie_analise = load_lottieurl(
    "https://assets7.lottiefiles.com/packages/lf20_u8jppxsl.json"
)
lottie_unificacao = load_lottieurl(
    "https://assets1.lottiefiles.com/packages/lf20_rvwumnmn.json"
)
lottie_interface = load_lottieurl(
    "https://assets6.lottiefiles.com/packages/lf20_xtvomr66.json"
)
lottie_brainstorm = load_lottieurl(
    "https://assets3.lottiefiles.com/packages/lf20_ayiupfed.json"
)
lottie_gamificacao = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_ldlns8rs.json"
)
lottie_ice = load_lottieurl(
    "https://assets1.lottiefiles.com/packages/lf20_3rqwsqnj.json"
)
lottie_politica = load_lottieurl(
    "https://assets7.lottiefiles.com/packages/lf20_udni1dqy.json"
)

# Imagens
image1 = Image.open("site quebrado.jpg")
image2 = Image.open("situação das metas.jpg")
image3 = Image.open("logo pne.png")

# Menu lateral
with st.sidebar:
    selected = option_menu(
        menu_title="Menu Principal:",
        options=[
            "Objetivo do projeto",
            "Dados Abertos",
            "Plano Nacional de Educação",
            "Evolução do Projeto",
            "Divisão das funções",
            "Análise Estatística",
            "Dashboard",
        ],
        menu_icon="cast",
        default_index=0,
    )

# Header
if selected == "Objetivo do projeto":
    st.title("Objetivo do projeto:")
    st.header("Monitoramento das Metas da PNE")
    st.write(
        "**Realizar o monitoramento das metas do Plano Nacional de Educação (PNE) por meio de análises estatísticas e democratizar o acesso aos seus dados**"
    )
    st.write("---")
    st.image(image1, width=1080)
    st.write(
        "**[Link de acesso>](https://simec.mec.gov.br/pde/relatorioMonitoramento.php)**"
    )
    st.write("---")
    st.image(image2, width=1080)
    st.write(
        "**[Link de acesso>](https://pne.mec.gov.br/18-planos-subnacionais-de-educacao/38-situacao-das-metas-dos-planos-de-)**"
    )

if selected == "Plano Nacional de Educação":
    st.title("O que é a PNE (Plano Nacional de Educação):")
    st.header(
        "O Plano Nacional de Educação (PNE) é uma Lei Federal nº 13.005/2014 com vigência decenal, que foi implementada no governo Dilma. Está de acordo com o artigo 214 da constituição. Suas diretrizes são:"
    )
    st.write("**I - erradicação do analfabetismo**")
    st.write("**II - universalização do atendimento escolar**")
    st.write("**III - melhoria da qualidade do ensino**")
    st.write("**V - promoção humanística, científica e tecnológica do País.**")
    st.write(
        "**VI - estabelecimento de meta de aplicação de recursos públicos em educação como proporção do produto interno bruto. (Incluído pela Emenda Constitucional nº 59, de 2009)**"
    )
    st.image(image3)

if selected == "Dados Abertos":
    st.title("As cinco estrelas dos dados abertos: ⭐ ⭐ ⭐ ⭐ ⭐")
    st.write(
        "**Em 2010, o cientista britânico Tim Berners-Lee, inventor da Web, formulou um sistema de estrelas para encorajar a sociedade, especialmente guardiões de dados governamentais, a abrirem seus dados. O sistema ajuda a diagnosticar o nível de abertura de dados dos órgãos públicos e fornece degraus alcançáveis para se chegar a níveis cada vez mais refinados de dados abertos.**"
    )
    st.write(
        "**⭐ Publicar bases na Web (em qualquer formato) com licença aberta < -- Começamos aqui: [Link de acesso>](https://download.inep.gov.br/publicacoes/institucionais/plano_nacional_de_educacao/relatorio_do_quarto_ciclo_de_monitoramento_das_metas_do_plano_nacional_de_educacao.pdf)**"
    )
    st.write(
        "**⭐ ⭐ Publicar bases em formato estruturado com licença aberta (ex: arquivo Excel, em vez de imagem escaneada)**"
    )
    st.write(
        "**⭐ ⭐ ⭐ Usar formatos não proprietários e uma licença aberta (ex: arquivo CSV em vez de Excel)**"
    )
    st.write(
        "**⭐ ⭐ ⭐ ⭐ Usar URLs para descrever coisas, para que qualquer um possa identificá-las < -- Conclusão: [Link de acesso>](https://metaspne.herokuapp.com/)**"
    )
    st.write("**⭐ ⭐ ⭐ ⭐ ⭐ Conectar seus dados a outras bases para dar contexto**")
    st_lottie(lottie_database, height=300)

if selected == "Divisão das funções":
    st.title("Divisão das funções:")
    st.header("Coleta dos Dados")
    st.write(
        "**Coletamos os Dados de bases públicas não estruturadas disponibilizadas pelo governo. Disponibilidade de dados públicos para o usuário**"
    )
    st_lottie(lottie_exploracao, height=300)
    st.write("---")
    st.header("Análise exploratória das metas")
    st.write(
        "**Análisamos as 20 Metas definidas pela PNE, observamos padrões e definimos pontos focais para o projeto**"
    )
    st_lottie(lottie_analise, height=300)
    st.write("---")
    st.header("Estrutura unificada")
    st.write(
        "**Dividimos entre os membros do grupo as 20 metas para serem estruturadas e unificadas em um csv**"
    )
    st_lottie(lottie_unificacao, height=300)
    st.write("---")
    st.header("Construção do Dashboard e Site")
    st.write(
        "**Sumarizamos os Dados coletados em um Dashboard e construímos a interface de um site interativo [Link do código>](https://github.com/fabricio-inoue/metaspne/blob/master/pne.py)**"
    )
    st_lottie(lottie_interface, height=300)

if selected == "Evolução do Projeto":
    st.title("Evolução do Projeto:")
    st.header("Brainstorming")
    st_lottie(lottie_brainstorm, height=300)
    st.write("**Definir qual será o escopo do projeto e o que buscamos entregar:**")
    st.write("**- Buscar bases de dados em órgãos de confiança**")
    st.write("**- Explorando vários temas e buscando dados referentes aos mesmos**")
    st.write("**- Selecionando temas por relevância**")
    st.write("---")
    st.header("Histórico de Propostas:")
    st.subheader("Gamificação na educação")
    st_lottie(lottie_gamificacao, height=300)
    st.write(
        "**Gamificação na educação é uma denominação que tem sido cada vez mais utilizada nos ambientes escolares**"
    )
    st.write("**Problema: Dificuldade na implementação em território nacional**")
    st.write("---")
    st.subheader("Análise do ranking ICE")
    st_lottie(lottie_ice, height=300)
    st.write(
        "**O ranking geral do Índice de Cidades Empreendedoras (ICE) 2022 leva em consideração cada um dos sete determinantes - ambiente regulatório, infraestrutura, mercado, acesso a capital, inovação, capital humano e cultura - e seus indicadores**"
    )
    st.write(
        "**Problema: Mostra uma taxa de 0 a 10, mas não apresenta como foram levantadas as variáveis**"
    )
    st.write("---")
    st.subheader("Análise das propostas dos candidatos à presidência")
    st_lottie(lottie_politica, height=300)
    st.write(
        "**Reunir as propostas dos candidatos, categorizar as propostas e por fim, analisar a performance dos políticos que já possuem carreira política**"
    )
    st.write(
        "**Problema: Não encontramos dados mensuráveis o suficiente nas propostas**"
    )

if selected == "Dashboard":
    st.title("Dashboard:")
    components.iframe(
        "https://app.powerbi.com/view?r=eyJrIjoiMzlkZThhYjMtNjNhYS00ZDk5LWEzZTQtODhmMGI0MTJkZTk2IiwidCI6IjhlYjI5MjAxLWEyN2QtNDMwMi04NDczLWM5ODJlYjViZTkzNSJ9&pageName=ReportSection3abce68dfea4fa13512a",
        width=1400,
        height=850,
        scrolling=True,
    )

if selected == "Análise Estatística":
    st.title("Gráfico de Análise Estatística:")
    components.iframe(
        "https://public.flourish.studio/visualisation/11820257/",
        width=1400,
        height=850,
        scrolling=True,
    )
# %%


