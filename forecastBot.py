#!/usr/bin/python3
import os
import tweepy
import requests
from dotenv import load_dotenv
import datetime
import json

load_dotenv()

consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
my_station_id = os.getenv('WF_STATION_ID')
my_token = os.getenv('WF_TOKEN')
my_url = "https://swd.weatherflow.com/swd/rest/better_forecast?station_id={}&units_temp=f&units_wind=mph&units_pressure=inhg&units_precip=in&units_distance=mi&token={}".format(my_station_id, my_token)
dayOfMonth = datetime.datetime.today().day

#If the current time is after 6pm, get tomorrows forecast instead of today
isToday = 0
t = datetime.datetime.now().strftime("%H")
if int(t) > 18:
    isToday = 1

r = requests.get(my_url)
data = r.json()
conditions = data['forecast']['daily'][isToday]['conditions']
sunrise = data['forecast']['daily'][isToday]['sunrise']
sunset = data['forecast']['daily'][isToday]['sunset']
highTemp = data['forecast']['daily'][isToday]['air_temp_high']
lowTemp = data['forecast']['daily'][isToday]['air_temp_low']
precipProb = data['forecast']['daily'][isToday]['precip_probability']
if precipProb !=0:
    precipType = data['forecast']['daily'][isToday]['precip_type']

sunset = datetime.datetime.fromtimestamp(sunset)
sunrise = datetime.datetime.fromtimestamp(sunrise)
sunset = sunset.strftime("%I:%M %p")        
sunrise = sunrise.strftime("%I:%M %p")
highTemp = (str(int(highTemp))) + u'\N{DEGREE SIGN}'
lowTemp = (str(int(lowTemp))) + u'\N{DEGREE SIGN}'

if isToday == 0:
    msg = "Good Morning Lorain County!\n\nToday "
else:
    msg = "Good Evening Lorain County!\n\nTomorrow "

msg = msg + "will be {}\nHigh: {} Low: {}\n".format(conditions, highTemp, lowTemp) 
if precipProb != 0:
    msg = msg + "Chance of {} is {}%\n".format(precipType, precipProb)
else:
    msg = msg + "No chance of precipitation\n"
msg = msg + "Sunrise/set is at {}/{}".format(sunrise, sunset)
print(msg)
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status(msg)
