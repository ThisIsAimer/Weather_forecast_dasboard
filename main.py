import streamlit as web

web.title("Weather Forecast Dashboard")
place = web.text_input("place:",placeholder="Ex: Japan")
days = web.slider("Days:", 1, 5, help="Select the number of days you want the forecast of")
selection = web.selectbox("Type of data you want to view:",("Temperature","Weather"))

web.header(f"{selection} for the next {days} days in {place}:")
