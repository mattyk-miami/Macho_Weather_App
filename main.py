import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next Few Days")
place = st.text_input(placeholder="Enter a place", label="Place:", key="place")

days = st.slider(
    label="Select forecast days",
    min_value=1,
    max_value=5,
    value=3,    # Initial default value (must be an integer)
    step=1,     # Ensures movement only by whole numbers
    help="Number of days in forecast (1-5)"
)

selection = st.selectbox(
    label="Select data to view:",
    options=["Temperature", "Sky"],
    index=0,  # Sets the default selection (0 for the first option, 1 for the second)
    help="Select either temperature or sky"
)

st.subheader(f"{selection} for the next {days} day{'s' if days > 1 else ''} in {place.title()}")

try:
    if place:
        dates, temperatures, skies = get_data(place, days)

        # Create the figure object using plotly express
        fig = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (F)'})

        # Display the figure in Streamlit

        if selection == "Temperature":
            st.plotly_chart(fig, use_container_width=None)
        else:
            st.image(image=skies, caption=dates, width=85)
except KeyError:
    st.write("You entered a non-existent place or place with no data available.")