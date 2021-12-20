# https://docs.streamlit.io/en/stable/getting_started.html
# https://docs.streamlit.io/en/stable/api.html
# https://www.openstreetmap.org/#map=8/-13.553/-39.298
# https://www.opencyclemap.org/
# https://www.cyclosm.org/#map=12/-12.9654/-38.3862/cyclosm
# https://www.bicyclenetwork.com.au/tips-resources/maps-and-rides/bike-trail-maps/
# https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt
    # pip freeze?

# https://cNLw104.na1.hubspotlinks.com/Btc/ZT+113/cNLw104/VVWKXh2mdDRgW8hkpwZ1tlGkgVcSh174xcQpJMZjDWN3lScmV1-WJV7CgMNXW2zw67T83qr7nW3CVgRF2RR28RW79WDg68F5RvDW1nCXtN2cD6FrW3z6v7l49jpnRW4hs3Gh3DVMHJW24tXlS1YL8q5VLrKmf63ZPz0W7-YK5z4Cwt96W2CmFk76B5x5hW55p6Kl4Gh-rwW2RDj3T2CwXm4VNKS6f1BZ8LDW26cYBc444gcGW6h-qqL7zTZs0W3yznkC2N0D8GVXk7-Q8DhJ2sW3-Y96B5CwPXgN540zl29rm_GW393kqt8KQ4PNW3JM6LM1lJVY9W23FwgN4tnH6vW8Gnczh1YfzzvW8pllsj4MGWkZW3wPP4G4T-QjrW6GdMgN4yB7zS36CW1

# OBJETIVO:
    # FAZER CONSULTAS NO OPEN STREET MAP
    # CRIAR DATAFRAME E PLOTAR NO NOSSO MAPA

import numpy as np
import pandas as pd
import streamlit as st
import time

st.title("My first app")

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we\'re done!'

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    chart_data

# option = st.selectbox(
#     'Which number do you like best?',
#     df['first column'])

# 'You selected: ', option

option = st.sidebar.selectbox(
    'Which number do you like best?',
    df['first column'])

'You selected:', option


left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")
    st.echo("HELLO WORLD!")

expander = st.expander("FAQ")
expander.write(
    "Here you could put in some really, really long explanations...")
