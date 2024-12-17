import streamlit as web
import plotly.express as plotly

web.title("Weather Forecast Dashboard")
place = web.text_input("place:",placeholder="Ex: Japan")
days = web.slider("Days:", 1, 5, help="Select the number of days you want the forecast of")
selection = web.selectbox("Type of data you want to view:",("Temperature","Weather"))

web.header(f"{selection} for the next {days} days in {place}:")

dates = ["oct 1st","oct 5th", "oct 10th", "oct 15th", "oct 20"]
temperature = [20,19,22,19,16]



graph = plotly.line(x= dates, y= temperature, labels={"x":"Dates","y":"Temperature (C)"})
web.plotly_chart(graph)