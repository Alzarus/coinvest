# https://coinmarketcap.com/api/documentation/v1/#tag/cryptocurrency

import json
import numpy as np
import pandas as pd
import requests
import streamlit as st
import time

# st.title("Dashboard - criptomoedas por CoinMarketCap - https://coinmarketcap.com/ ")

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })

base_url = "https://pro-api.coinmarketcap.com"
url = base_url + "/v1/cryptocurrency/listings/latest"
# url = base_url + "/v1/global-metrics/quotes/latest"

parameters = {
    'start': '1',
    'limit': '5',
    'convert': 'BRL'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '3a7e4762-73a0-455f-b6d7-e31098ffab37',
}

response = requests.get(url, headers=headers, params=parameters)
json_response = response.json()
print(json.dumps(json_response, indent=4))

# response_data = json_response["data"]
# print(json.dumps(response_data[0], indent=4))
# for r in response_data:
#     print(r["name"])


# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#         np.random.randn(20, 3),
#         columns=['a', 'b', 'c'])

#     chart_data

# option = st.sidebar.selectbox(
#     'Which number do you like best?',
#     df['first column'])

# 'You selected:', option


# left_column, right_column = st.columns(2)
# pressed = left_column.button('Press me?')
# if pressed:
#     right_column.write("Woohoo!")
#     st.echo("HELLO WORLD!")

# expander = st.expander("FAQ")
# expander.write(
#     "Here you could put in some really, really long explanations...")
