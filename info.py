#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands
import os
import sys
import time
import pcd8544 as lcd
import pcd8544_ext as lcd_ext

import pi_logo
import clock
from sys_info import show_sys_info
import weather
import earthquake

def show_info():
    lcd.draw_bitmap(pi_logo.LOGO)
    time.sleep(5)
    lcd.draw_bitmap(pi_logo.NAME)
    time.sleep(5)
    
    clock.show_bg(lcd.draw_bitmap)
    clock.show_time(lcd_ext.shake_display_words)
    time.sleep(1)
    
    show_sys_info(lcd.display_words)
    
    lcd_ext.shake_display_words(weather.get_current_weather('shanghai'), 2) # get current weather
    time.sleep(2)
    
    for w in weather.get_forecast_weather('shanghai', 7): # get 7days forecast weather
        lcd_ext.shake_display_words(w, 2)
        time.sleep(2)
        
    earthquake.show_earthquake(lcd_ext.alarm_marquee_display_words)
    time.sleep(5)
    
if __name__ == "__main__":
  lcd.init()
  lcd.light(1)
  while 1:
    show_info()
