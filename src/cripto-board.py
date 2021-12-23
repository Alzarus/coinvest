# https://coinmarketcap.com/api/documentation/v1/#tag/cryptocurrency
# https://docs.streamlit.io/library/api-reference

import json
import numpy as np
import pandas as pd
import requests
import streamlit as st
import time

st.title("Dashboard - criptomoedas por CoinMarketCap\nhttps://coinmarketcap.com/ ")

BASE_URL = "https://pro-api.coinmarketcap.com"
URL = BASE_URL + "/v1/cryptocurrency/listings/latest"
# URL = BASE_URL + "/v1/global-metrics/quotes/latest"
INVESTIMENT_TERM = st.radio(
    "Prazo de investimento escolhido:", ('Curto prazo', 'Médio prazo', 'Longo prazo'))
if INVESTIMENT_TERM:
    st.write(f"Escolheu o {INVESTIMENT_TERM}")

CRYPTO_LIMIT = st.slider(
    "Quantidade de criptomoedas a serem exibidas:", min_value=1, max_value=50, value=5)
PARAMETERS = {
    'start': '1',
    'limit': str(CRYPTO_LIMIT),
    'convert': 'BRL'
}
HEADERS = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '3a7e4762-73a0-455f-b6d7-e31098ffab37',
}


def load_data():
    response = requests.get(URL, headers=HEADERS, params=PARAMETERS)
    json_response = response.json()
    # print(json.dumps(json_response, indent=4))
    return json_response


st.json(load_data())
