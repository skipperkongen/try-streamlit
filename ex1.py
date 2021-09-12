import time

import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

"""
# My first app
> Magic!
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.sidebar.write('Settings')

if st.sidebar.checkbox('Show dataframe'):
    st.write(df)

if st.sidebar.checkbox('Show line chart'):
    st.line_chart(chart_data)

if st.sidebar.checkbox('Show map'):
    st.map(map_data)

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'Number selected: ', option

value = st.sidebar.slider('Values')

'Value selected', value

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
