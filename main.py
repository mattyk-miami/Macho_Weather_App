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

# selection = st.selectbox(
#     label="Select data to view:",
#     options=["Temperature", "Sky"],
#     index=0,  # Sets the default selection (0 for the first option, 1 for the second)
#     help="Select either temperature or sky"
# )

# st.subheader(f"{selection} for the next {days} day{'s' if days > 1 else ''} in {place.title()}")

try:
    if place:
        st.subheader(f"Temperature for the next {days} day{'s' if days > 1 else ''} in {place.title()}")
        dates, temperatures, feels_like, skies, sky_description = get_data(place, days)
        captions = []
        for i in range(len(dates)):
            captions.append(f"<b>{sky_description[i].title()}</b><br>{dates[i]}")

        # Create the figure object using plotly express
        fig = px.line(x=dates, y=[temperatures, feels_like], labels={'x': 'Date', 'value': 'Temperature (F)'},
                      color_discrete_sequence=['#1f77b4', '#ff7f0e'])
        # Rename the legend traces for clarity
        names = {'wide_variable_0': 'Temperature', 'wide_variable_1': 'Feels Like'}
        fig.for_each_trace(lambda t: t.update(name=names.get(t.name, t.name)))

        # Display the figure in Streamlit

        # if selection == "Temperature":
        st.plotly_chart(fig, use_container_width=None)
        # else:
            # Total number of images you have
        total_images = len(skies)
        images_per_row = 8

        st.subheader(f"Sky for the next {days} day{'s' if days > 1 else ''} in {place.title()}")
        # Loop through your images in steps of 8
        for row_idx in range(0, total_images, images_per_row):

            # Slice the data for just the current row (up to 8 items)
            row_images = skies[row_idx: row_idx + images_per_row]
            row_captions = captions[row_idx: row_idx + images_per_row]

            # Dynamically create exactly enough columns for this row (max 8)
            cols = st.columns(len(row_images))

            # Render the images and captions side-by-side in this row
            for col, img, cap in zip(cols, row_images, row_captions):
                with col:
                    st.image(img, width="stretch")
                    st.markdown(
                        f"<div style='text-align: center; font-size: 0.85rem;'>{cap}</div>",
                        unsafe_allow_html=True
                    )


            # st.image(image=skies, caption=captions, width=85)
except KeyError:
    st.write("You entered a non-existent place or place with no data available.")