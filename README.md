# Twitter weather bot for the Weatherflow API
These programs are intended to utilize the WeatherFlow and Twitter APIs to post tweets to a Twitter page.

## Requirements
You will need
- A twitter account that is enrolled as a twitter developer account
- To be approved for "Elevated" access.  When you sign up, your account will be "Essential".  You will need to fill out a short application for review.  In my case, it took about 4 hours to get approved once I applied.  https://developer.twitter.com/en/portal/products/elevated
- The Tweepy API installed.  https://docs.tweepy.org/en/stable/

## Twitter developer account needs
- Create a twitter page that you want to post as
- Setup your developer account https://developer.twitter.com/en/portal/dashboard
- Craete a new project/app.
- Fill in the required fields
- For keys and tokens, you'll need
  - Consumer Key: API KEY and API KEY Secret
  - Authintication tokens: ACCESS_TOKEN and ACCESS_TOKEN_SECRET
  
## WeatherFlow developer
You will need to get an access token from WeatherFlow along with your device and station IDs.  To get the token, log into your account at tempestws.com and go to setting -> Data Authorizations - Create token.  Save this value.  To get your device and station IDs, from the main acount screen, select the Tempest icon in the top right to bring up your device.  Then at the bottom right of the page, click on "Online".  You can get those values from the following tables.
  
## Setup your environment
- Save the keys in a ".env" file in your program directory.  
```
TW_API_KEY=" "
TW_API_KEY_SECRET=" "
TW_ACCESS_TOKEN=" "
TW_ACCESS_TOKEN_SECRET=" "
WF_DEVICE_ID=" "
WF_STATION_ID=" "
WF_TOKEN=" "

The conditionsBot.py program gets current observations from your device and tweets them to the Twitter Page.
The forecastBot.py program will get and tweet the current day's forecast if the time is less than 6pm or tomorrows forecast if after.

I have both of these programms getting run out of cron and specific times.
  
 
