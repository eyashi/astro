import requests
import configparser

keys = configparser.ConfigParser()
keys.read('keys.ini')

api_key = keys["weather"]["apikey"]

endpoint = "http://api.openweathermap.org/data/2.5/weather"
headers = {'Content-Type': 'application/json'}
params = {'id':'2172797', 'appid':api_key}

resp = requests.get(endpoint, params=params)

print(resp.text)
