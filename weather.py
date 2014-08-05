#!/usr/bin/python
# -*- coding: utf-8 -*-
from web_message_client import RestGet as restget
import weather_icon as icon
import sys
import time

URL = 'http://api.worldweatheronline.com/free/v1/weather.ashx?q={0:s}&format=json&num_of_days={1:d}&key='
APP_KEY = '56b90927c9d71d70311517c9f85ccaca13c5b4b2'
WEATHER = None
CURRENT_WEATHER = None
FORECAST_WEATHERS = None
ABS_ZORE_TEMP = 273.15
UPDATE_INTERVAL = 30 # in min


def __format_weather_result__(weather):
    data = weather['data']
    current = data['current_condition'][0]
    forecast = []
    for f in data['weather']:
        forecast.append(['---Forecast---',
                         data['request'][0]['query'],
                         '  {:s}  '.format(f['date']),
                         f['weatherDesc'][0]['value'],
                         'T:{0:.1f}~{1:.1f} {2:s}C'.format(float(f['tempMinC']), float(f['tempMaxC']), chr(167)),
                         'Win: {0:s}{1:.0f}{2:s} {3:.0f}KM/h'.format(f['winddir16Point'], float(f['winddirDegree']), chr(167), float(f['windspeedKmph']))])
        
    return {"current" : ['---Weather--- ',
                         data['request'][0]['query'],
                         current['weatherDesc'][0]['value'],
                         'T:{0:.1f} {1:s}C'.format(float(current['temp_C']), chr(167)),
                         'Hum:{:.0f}%'.format(float(current['humidity'])),
                         'Win: {0:s}{1:.0f}{2:s} {3:.0f}KM/h'.format(current['winddir16Point'], float(current['winddirDegree']), chr(167), float(current['windspeedKmph']))],
            "forecast" : forecast}
            
def __get_weather__(city, days = 5):
    global WEATHER
    
    days = max(min(5, days), 1)
    url = URL.format(city, days) + APP_KEY
    current_min = time.localtime().tm_min
    if WEATHER == None or current_min % UPDATE_INTERVAL == 0:
        w = restget(url, {'Content-Type': "application/json"})
        if w == "": return WEATHER
        WEATHER = __format_weather_result__(w)

    return WEATHER

if __name__ == "__main__":
    print __get_weather__("Shanghai", 3)
