
import json
import requests
import os
import streamlit as st



env= os.environ
lattitude= env['LAT']
longitude=env['LONG']
api_key=env['API_KEY']


st.title('NoWeather')
url = "http://api.openweathermap.org/data/2.5/weather?"
url = url + "lat=" + lattitude + "&lon=" + longitude + "&appid=" + api_key
response = requests.get(url)
data = json.loads(response.text)




st.write(data)
