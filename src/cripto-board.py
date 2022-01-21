# https://coinmarketcap.com/api/documentation/v1/#tag/cryptocurrency
# https://docs.streamlit.io/library/api-reference

import json
# from turtle import title
import numpy as np
import pandas as pd
import requests
import streamlit as st
import time

BASE_URL = "https://pro-api.coinmarketcap.com"
URL = BASE_URL + "/v1/cryptocurrency/listings/latest"
# URL = BASE_URL + "/v1/global-metrics/quotes/latest"
INVESTIMENT_TERM = ""
CRYPTO_LIMIT = ""
CONVERT_CURRENCY = ""
PARAMETERS = {
    'start': '1',
    'limit': "",
    'convert': ""
}
HEADERS = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '3a7e4762-73a0-455f-b6d7-e31098ffab37',
}


# @st.cache
def load_data():
    global HEADERS, PARAMETERS

    response = requests.get(URL, headers=HEADERS, params=PARAMETERS)
    json_response = response.json()
    total_coins = json_response["status"]["total_count"]
    # print(json.dumps(json_response, indent=4))
    json_response_data = json_response["data"]
    for data in json_response_data:
        data.pop("tags", None)
    return json_response_data


def load_sidebar():
    global INVESTIMENT_TERM, CRYPTO_LIMIT, CONVERT_CURRENCY, PARAMETERS

    st.sidebar.title("Opções")

    INVESTIMENT_TERM = st.sidebar.radio(
        "Prazo de investimento escolhido:", ('Curto prazo', 'Médio prazo', 'Longo prazo'))
    # if INVESTIMENT_TERM:
    #     st.sidebar.write(f"Escolheu o {INVESTIMENT_TERM}")

    CRYPTO_LIMIT = st.sidebar.slider(
        "Quantidade de criptomoedas a serem exibidas:", min_value=1, max_value=50, value=5)

    CONVERT_CURRENCY = st.sidebar.selectbox(
        "Moeda de conversão escolhida:", ("BRL", "USD"))

    PARAMETERS = {
        'start': '1',
        'limit': str(CRYPTO_LIMIT),
        'convert': f"{CONVERT_CURRENCY}"
    }

    st.sidebar.title("Sobre")
    st.sidebar.info("Este dashboard é fruto do projeto de TCC do estudante de Análise"
                    " e Desenvolvimento de Sistemas pelo IFBA - Campus Salvador:\n\n"
                    "Pedro Batista de Almeida Filho")


def main():
    # st.title("Dashboard - criptomoedas por CoinMarketCap\nhttps://coinmarketcap.com/ ")
    st.title("Investcrip - Dashboard para o seu investimento em Criptomoedas\n\nFonte dos dados: https://coinmarketcap.com/ ")
    load_sidebar()
    # TODO: CRIAR DATA FRAME COM TODOS OS OBJETOS (MOEDAS) DA LISTA, APENAS PEGANDO OS DADOS QUE TENHO INTERESSE
    # TODO: CRIAR METODO ASYNC PARA ATUALIZAR O BOARD AUTOMATICAMENTE DPS DE X SEGUNDOS/MINUTOS
    # TODO: REQUESTS -> BANCO DE DADOS -> MS DO DASH BUSCA NO BANCO DE DADOS (EVITAR A QUANTIDADE DE REQUESTS ELEVADA)
    # https://github.com/paduel/streamlit_finance_chart/blob/master/app.py
    # components = pd.DataFrame({
    #     'first column': [1, 2, 3, 4],
    #     'second column': [10, 20, 30, 40]
    # })
    # st.dataframe(components)
    st.json(load_data())


if __name__ == '__main__':
    main()
