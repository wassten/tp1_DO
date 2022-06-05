
import json
import requests
import os



env= os.environ
lattitude= env['LAT']
longitude=env['LONG']
api_key=env['API_KEY']



url = "http://api.openweathermap.org/data/2.5/weather?"
url = url + "lat=" + lattitude + "&lon=" + longitude + "&appid=" + api_key
response = requests.get(url)
data = json.loads(response.text)




print(data)
