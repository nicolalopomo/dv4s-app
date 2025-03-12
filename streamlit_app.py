import streamlit as st

# Title
st.title('My New Streamlit App!')

# Text
st.write('Welcome to my new app!')

# Data
data = st.slider('Select a value', 0, 100, 50)
st.write('You selected:', data)