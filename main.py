import streamlit as web
import plotly.express as plotly
import backend

web.title("Weather Forecast Dashboard")
place = web.text_input("place:",placeholder="Ex: Japan")
days = web.slider("Days:", 1, 5, help="Select the number of days you want the forecast of")
selection = web.selectbox("Type of data you want to view:",("Temperature","Weather"))

web.header(f"{selection} for the next {days} days in {place}:")


if place:
    # get temp and sky data
    filtered_data = backend.get_data(place,days,selection)


if place:
    if selection == "Temperature":
        temperature = [dicts["main"]["temp"] for dicts in filtered_data]
        dates = [dicts["dt_txt"] for dicts in filtered_data]
        graph = plotly.line(x= dates, y= temperature , labels={"x":"Dates","y":"Temperature (C)"})
        web.plotly_chart(graph)

    if selection == "Weather":
        images = {"Clear": "images/clear.png","Clouds": "images/cloud.png","Rain": "images/rain.png","Snow": "images/snow.png",}
        conditions = [dicts["weather"][0]["main"] for dicts in filtered_data]
        image_paths = [images[condition] for condition in conditions]

        web.image(image_paths ,width= 100 )