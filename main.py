import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


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

# # Create some random mock data
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['Option A', 'Option B', 'Option C']
# )
#
# # Display a line chart
# st.line_chart(chart_data)
#
# # Sample data
# df = pd.DataFrame({
#     "Category": ["X", "Y", "Z"],
#     "Values": [10, 15, 7]
# })

dates = ['2026-08-22', '2026-08-23', '2026-08-24']
temperatures = [90.5, 91.2, 92.3]
# Create the figure object using plotly express
fig = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (F)'})

# Display the figure in Streamlit
st.plotly_chart(fig, use_container_width=None)