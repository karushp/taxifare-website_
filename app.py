import streamlit as st
import datetime
import requests

'''
## ESTIMATE YOUR TAXI FARE
'''

st.image('OIG3.jpg')

col1, col2, col3 = st.columns([1, 1,1])
with col1:
    date = st.date_input(
        "Select a date"
    )

with col2:
    time = st.time_input("Select Time")

with col3:
    passenger_count = st.number_input("No. of Passengers", 1)


columns = st.columns(4)

pickup_lon = columns[0].number_input("Pickup Longitude", value=40.7614327)
columns[0].write(pickup_lon)

pickup_lat = columns[1].number_input("Pickup Latitute", value=-73.9798156)
columns[1].write(pickup_lat)

dropoff_lon = columns[2].number_input("Dropoff Longitude", value=40.6513111)
columns[2].write(dropoff_lon)

dropoff_lat = columns[3].number_input("Dropoff Latitude", value=-73.8803331)
columns[3].write(dropoff_lat)


url = 'https://taxifare.lewagon.ai/predict'


parameters = {
              'pickup_datetime' : f'{date} {time}',
              'pickup_longitude' : pickup_lon,
              'pickup_latitude' : pickup_lat,
              'dropoff_longitude' : dropoff_lon,
              'dropoff_latitude' : dropoff_lat,
              'passenger_count': int(passenger_count)
              }

response = requests.get(url, params=parameters).json()


result = st.button("Calculate")
if result:
    st.write('Your estimated fare is :$',round(response['fare'],2))
