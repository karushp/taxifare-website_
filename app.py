import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''



date = st.date_input(
    "Select a date",
    datetime.date(2024, 5,17))

time = st.time_input('Select preferred time', datetime.time(8, 45))

st.write('date', f'{date} {time}')



pickup_log = st.number_input('Specify pickup LOGITUDE?', 3.4444)
pickup_lat =st.number_input('Specify pickup LATITUDE?', 43344566.23456)
dropoff_lon= st.number_input('Specify dropoff LONGITUTE?')
dropoff_lat=st.number_input('Specify dropoff LATITUDE?')
passenger_count=st.number_input('How many passengers are travelling?')

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

parameters = {
              'pickup_datetime' : f'{date} {time}',
              'pickup_longitude' : pickup_log,
              'pickup_latitude' : pickup_lat,
              'dropoff_longitude' : dropoff_lon,
              'dropoff_latitude' : dropoff_lat,
              'passenger_count': int(passenger_count)
              }

response = requests.get(url, params=parameters).json()

st.write('Your estimated fare is :$',round(response['fare'],2))
