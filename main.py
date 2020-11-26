import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from vega_datasets import data

st.title('Sample Project')

st.text('This project is to practis usage of "streamlit" module. It\'s easy and first Webapp writen in python. ')

st.subheader('Cars dataframe')
cars = data.cars()
st.dataframe(cars)

st.subheader('Chart with altair')

brush = alt.selection(type='interval')

base = alt.Chart(cars).mark_circle(size=60).add_selection(brush).properties(
    width=500,
    height=400
)

car_chart = base.encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color=alt.condition(brush, 'Origin', alt.ColorValue('gray')),
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
)

cars_categories = base.encode(
    x='Origin:N',
    y='Cylinders:O',
    color=alt.condition(brush, 'Origin', alt.ColorValue('gray')),
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
)

chart = car_chart | cars_categories
st.write(chart)

st.subheader('Map')

data = pd.DataFrame({
    'awesome cities': ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat': [41.868171, 44.979840,  38.257972, 39.030575],
    'lon': [-87.667458, -93.272474, -85.765187,  -95.702548]
})

st.map(data)

st.subheader('Check box')

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)


st.subheader('Inserted widgets pinned to left.')
st.sidebar.markdown('# This is sidebar header')
option = st.sidebar.selectbox(
    'Which number of Cylinders do you like best?',
    cars['Cylinders'])

'You selected:', option

st.sidebar.markdown('You selected: {}'.format(option))
slid_val = st.sidebar.slider('slide_val')
