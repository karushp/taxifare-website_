import streamlit as st
import numpy as np
import pandas as pd
import requests


st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
    .title {
        font-family: 'Roboto', sans-serif;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)


# Centered title with custom font
st.markdown("<h1 class='title'> Estimate your Taxi Fare</h1>", unsafe_allow_html=True)




# header image
st.image('ny_taxi.jpg')

# columns for Date, time and Passenger Count
col1, col2, col3 = st.columns([1, 1,1])
with col1:
    date = st.date_input(
        "Select Date"
    )

with col2:
    time = st.time_input("Select Time")

with col3:
    passenger_count = st.number_input("No. of Passengers", 1)


# Columns for Pickup and Dropoff Lat & Lon
columns = st.columns(4)
pickup_lon = columns[0].number_input("Pickup Longitude", value=40.7614327)
pickup_lat = columns[1].number_input("Pickup Latitute", value=-73.9798156)
dropoff_lon = columns[2].number_input("Dropoff Longitude", value=40.6513111)
dropoff_lat = columns[3].number_input("Dropoff Latitude", value=-73.8803331)

#url for api
url = 'https://taxifare.lewagon.ai/predict'

#parameters for prediction in model
parameters = {
              'pickup_datetime' : f'{date} {time}',
              'pickup_longitude' : pickup_lon,
              'pickup_latitude' : pickup_lat,
              'dropoff_longitude' : dropoff_lon,
              'dropoff_latitude' : dropoff_lat,
              'passenger_count': int(passenger_count)
              }

response = requests.get(url, params=parameters).json()

# Button for calculating
result = st.button("Calculate")
if result:
    st.write('Your estimated fare is :$',round(response['fare'],2))


#creating DataFrame for Map plot
df = pd.DataFrame({
    'lon': [pickup_lat, dropoff_lat],
    'lat': [pickup_lon, dropoff_lon]
})

# Display the map
st.map(df)


'''
#### beta version - only available for NY

'''
