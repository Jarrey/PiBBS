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
import sys_info
import weather
import earthquake

def show_info():
    #pi_logo.show_logo()
    
    #clock.show_time()
    
    sys_info.show_sys_info()
    
    weather.show_weather("Shanghai", 5)
       
    earthquake.show_earthquake()
    
if __name__ == "__main__":
  lcd.init()
  lcd.light(1)
  while 1:
    show_info()
