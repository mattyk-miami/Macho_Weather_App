import streamlit as st
import pandas as pd


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

if days > 1:
    plural = 's'
else:
    plural = ''

st.subheader(f"{selection} for the next {days} day{plural} in {place.title()}")