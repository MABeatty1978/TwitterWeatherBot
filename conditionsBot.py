#!/usr/bin/python3

import requests
import datetime
import json
import time
import os
from dotenv import load_dotenv
from datetime import datetime
import tweepy

load_dotenv()

consumer_key = os.getenv('TW_API_KEY')
consumer_secret = os.getenv('TW_API_KEY_SECRET')
access_token = os.getenv('TW_ACCESS_TOKEN')
access_token_secret = os.getenv('TW_ACCESS_TOKEN_SECRET')


device_id = os.getenv('WF_DEVICE_ID')
station_id = os.getenv('WF_STATION_ID')
token_id = os.getenv('WF_TOKEN')
my_time = datetime.now().strftime("%I:%M%p")
station_url = "https://swd.weatherflow.com/swd/rest/observations/station/{}?token={}".format(station_id, token_id)
device_url = "https://swd.weatherflow.com/swd/rest/observations/device/{}?token={}".format(device_id, token_id)
s = requests.get(station_url)
s_data = s.json()
d = requests.get(device_url)
d_data = d.json()

trend = d_data['summary']['pressure_trend']
last_lightning = d_data['summary']['strike_last_epoch']
lightning_distance = d_data['summary']['strike_last_dist']
temp = s_data['obs'][0]['air_temperature']
pressure = s_data['obs'][0]['barometric_pressure']
humidity = s_data['obs'][0]['relative_humidity']
precip = s_data['obs'][0]['precip']
wind_avg = s_data['obs'][0]['wind_avg']
wind_dir = s_data['obs'][0]['wind_direction']
wind_gust = s_data['obs'][0]['wind_gust']
radiation = s_data['obs'][0]['solar_radiation']
uv = s_data['obs'][0]['uv']
brightness = s_data['obs'][0]['brightness']
feels_like = s_data['obs'][0]['feels_like']
wind_chill = s_data['obs'][0]['wind_chill']

last_lightning = datetime.fromtimestamp(last_lightning).strftime("%d/%m %I:%M:%S%p")

temp = (str(int(temp * 1.8 + 32))) + u'\N{DEGREE SIGN}'
feels_like = (str(int(feels_like * 1.8 + 32))) + u'\N{DEGREE SIGN}' 
wind_chill = (str(int(wind_chill * 1.8 + 32))) + u'\N{DEGREE SIGN}' 
wind_avg = int(wind_avg * 2.2)
wind_gust = int(wind_gust * 2.2)
pressure = (str(int(pressure))) + "mb"
humidity = str(humidity)+"%"
if wind_dir > 348:
    wind_dir = "N"
elif wind_dir > 326:
    wind_dir = "NNW"
elif wind_dir > 303:
    wind_dir = "NW"
elif wind_dir > 281:
    wind_dir = "WNW"
elif wind_dir > 258:
    wind_dir = "W"
elif wind_dir > 236:
    wind_dir = "WSW"
elif wind_dir > 213:
    wind_dir = "SW"
elif wind_dir > 191:
    wind_dir = "SSW"
elif wind_dir > 168:
    wind_dir = "S"
elif wind_dir > 146:
    wind_dir = "SSE"
elif wind_dir > 123:
    wind_dir = "SE"
elif wind_dir > 101:
    wind_dir = "ESE"
elif wind_dir > 78:
    wind_dir = "E"
elif wind_dir > 56:
    wind_dir = "ENE"
elif wind_dir > 33:
    wind_dir = "NE"
elif wind_dir > 11:
    wind_dir = "NNE"
else:
    wind_dir = "N"

if uv >= 8:
    uv = str(uv) + " - VERY HIGH"
elif uv >= 6:
    uv = str(uv) + " - HIGH"
elif uv >= 3:
    uv = str(uv) + " - MODERATE"
else:
    uv = str(uv) + " - LOW"

msg = "Current Conditions - {}\nTemp: {}".format(my_time, temp)
if temp != feels_like:
    msg = msg + "\nFeels Like: {}".format(feels_like)
if temp != wind_chill:
    msg = msg + "\nWind Chill: {}".format(wind_chill)

msg = msg + "\nPressure is {} and {}\nWind: {} {}mph\nWind Gust: {}mph\nUV Index: {}\nLast Lightning Strike:\n{}, {} miles away".format(pressure, trend,  wind_dir, wind_avg, wind_gust, uv, last_lightning, lightning_distance ) 
print(msg)
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status(msg)
