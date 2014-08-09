#!/usr/bin/python
# -*- coding: utf-8 -*-
from web_message_client import RestGet as restget
import weather_icon as icon
import pcd8544 as lcd
import pcd8544_ext as lcd_ext
import sys
import time

URL = 'http://api.worldweatheronline.com/free/v1/weather.ashx?q={0:s}&format=json&num_of_days={1:d}&key='
APP_KEY = '56b90927c9d71d70311517c9f85ccaca13c5b4b2'
WEATHER = None
UPDATE_INTERVAL = 30 # in min


def __format_weather_result__(weather, city):
    data = weather['data']
    current = data['current_condition'][0]
    forecast = []
    for f in data['weather']:
        forecast.append(['---Forecast---',
                         '  {:s}  '.format(f['date']),
                         f['weatherDesc'][0]['value'],
                         'T:{0:d}~{1:d} {2:s}C'.format(int(f['tempMinC']), int(f['tempMaxC']), chr(167)),
                         'Win:{0:s}{1:.0f} {2:s}'.format(f['winddir16Point'], float(f['winddirDegree']), chr(167)),
                         'Spd:{:.0f} KM/h'.format(float(f['windspeedKmph']))])
        
    return {"current" : [" " * ((14 - len(city)) // 2) + city.upper(),
                         current['weatherDesc'][0]['value'],
                         'T:{0:d} {1:s}C'.format(int(current['temp_C']), chr(167)),
                         'Hum:{:.0f}%'.format(float(current['humidity'])),
                         'Win:{0:s}{1:.0f} {2:s}'.format(current['winddir16Point'], float(current['winddirDegree']), chr(167)),
                         'Spd:{:.0f} KM/h'.format(float(current['windspeedKmph']))],
            "weather_code": current['weatherCode'],
            "temp": int(current['temp_C']),
            "forecast" : forecast}
            
def __get_weather__(city, days = 5):
    global WEATHER
    
    days = max(min(5, days), 1)
    url = URL.format(city, days) + APP_KEY
    current_min = time.localtime().tm_min
    if WEATHER == None or current_min % UPDATE_INTERVAL == 0:
        w = restget(url, {'Content-Type': "application/json"})
        if w == "": return WEATHER
        WEATHER = __format_weather_result__(w, city)

    return WEATHER

def show_weather(city, days = 5):
    w = __get_weather__(city, days)
    
    # show graphic weather
    hur = time.localtime().tm_hour
    lcd.draw_bitmap(icon.WEATHER_ICONS[(w['weather_code'] + "N") if hur >= 18 or hur < 6 else w['weather_code']], w = 42, h = 48)
    
    if w['temp'] < 0:
        lcd.draw_bitmap(icon.MINUS, x = 42, w = 14, h = 24)
    else:
        lcd.draw_bitmap(icon.BLANK, x = 42, w = 14, h = 24)
    
    lcd.draw_bitmap(icon.NUMBERS[w['temp'] // 10], x = 56, w = 14, h = 24)
    lcd.draw_bitmap(icon.NUMBERS[w['temp'] % 10], x = 70, w = 14, h = 24)
    lcd.draw_bitmap(icon.C_DEGREE, x = 42, y = 3, w = 42, h = 24)
    time.sleep(10)
    
    # show current weather
    lcd_ext.shake_display_words(w['current'], 1)
    time.sleep(5)
    
    # show forecast weather
    for fw in w['forecast']:
        lcd_ext.shake_display_words(fw, 2)
        time.sleep(5)