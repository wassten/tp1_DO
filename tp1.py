
import json
import requests
import os
import streamlit as st
from datetime import datetime



env= os.environ
lattitude= env['LAT']
longitude=env['LONG']
api_key=env['API_KEY']


url = "http://api.openweathermap.org/data/2.5/weather?"
url = url + "lat=" + lattitude + "&lon=" + longitude + "&appid=" + api_key + "&units=metric"
response = requests.get(url)
data = json.loads(response.text)

icon = 'http://openweathermap.org/img/wn/' + str(data['weather'][0]['icon'])  + '@2x.png'

st.set_page_config(page_title=str(data['name']) +"'s Weather", page_icon = '☀️', layout = 'centered', initial_sidebar_state = 'auto')


st.title('Welcome to ' + data['name'])
st.write(' (' 
+ str(data['coord']['lon'])+ ', '+ str(data['coord']['lat'])+')')
st.text("")
st.text("")
col1, col2, col3, col4 = st.columns(4)

col1.image(icon)
col2.metric("Weather",str(data['weather'][0]['main']),str(data['weather'][0]['description']),delta_color="off")
col3.metric("Temperature", str(data['main']['temp']) + '° C', "Max : " + str(data['main']['temp_max']) + '°')
col4.metric("Wind", str(data['wind']['speed']) + ' m/s', str(data['wind']['deg']) + ' °')

sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%Hh %M')
sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Hh %M')
st.text("")
col11, col22, col33, col44,coll5 = st.columns(6)

col11.metric("",sunrise,"Sunrise",delta_color="off")
col33.image("https://c.tadst.com/gfx/1200x630/sun-calculator2.png?1")
col4.metric("",sunset,"-Sunset",delta_color="off")

st.text("")
with st.expander("See plain json source"):
    st.write(data)
