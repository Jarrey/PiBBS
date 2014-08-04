#!/usr/bin/python
# -*- coding: utf-8 -*-
from web_message_client import RestGet as restget
import time

APP_ID = '3a391364dffde4a1a3357a312ddc8646'
CURRENT_WEATHER = None
FORECAST_WEATHERS = None
ABS_ZORE_TEMP = 273.15
UPDATE_INTERVAL = 30 #min


def __format_weather_result__(weather):
    return ['---Weather--- ',
            '{0:s}-{1:s}'.format(weather[u'sys'][u'country'],weather[u'name']),
            '{:s}'.format(weather[u'weather'][0][u'main']),
            'T:{0:.1f} {1:s}C'.format(float(weather[u'main'][u'temp'])/10, chr(167)),
            'Hum:{:.1f}%'.format(float(weather[u'main'][u'humidity'])),
            'Win:{:.1f}m/s'.format(float(weather[u'wind'][u'speed']))]
            
def __format_forecast_result__(weather):
    weathers = []
    for day in weather[u'list']:
        weathers.append(['---Forecast---',
                         time.strftime('  %Y/%m/%d  ',time.localtime(day[u'dt'])),
                         '{:s}'.format(day[u'weather'][0][u'main']),
                         'T:{0:.1f}~{1:.1f} {2:s}C'.format(float(day[u'temp'][u'min']) - ABS_ZORE_TEMP, float(day[u'temp'][u'max']) - ABS_ZORE_TEMP, chr(167)),
                         'Hum:{:.1f}%'.format(float(day[u'humidity'])),
                         'Win:{:.1f}m/s'.format(float(day[u'speed']))])
    return weathers
            
def get_current_weather(city):
    global CURRENT_WEATHER, APP_ID, UPDATE_INTERVAL
    url = "http://api.openweathermap.org/data/2.5/weather?q={:s}&APPID=".format(city)+APP_ID    
    
    min = time.localtime().tm_min
    if CURRENT_WEATHER == None or min % UPDATE_INTERVAL == 0: 
        w = restget(url, {'Content-Type': "application/json"})
        if w == "": return CURRENT_WEATHER
        
        CURRENT_WEATHER = __format_weather_result__(w)
    
    return CURRENT_WEATHER
    
def get_forecast_weather(city, days = 5):
    global FORECAST_WEATHERS, APP_ID, UPDATE_INTERVAL
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?q={0:s}&cnt={1:d}&APPID=".format(city, days)+APP_ID
    
    if days > 16:
        days = 16
    if days < 1:
        days = 1
        
    min = time.localtime().tm_min
    if FORECAST_WEATHERS == None or min % UPDATE_INTERVAL == 0: 
        f = restget(url, {'Content-Type': "application/json"})
        if f == "": return FORECAST_WEATHERS
        
        FORECAST_WEATHERS = __format_forecast_result__(f)
        
    return FORECAST_WEATHERS