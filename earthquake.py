#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
import pickle
from web_message_client import RestGet as restget
import pcd8544 as lcd
import pcd8544_ext as lcd_ext

# earthquake API url
EARTHQUAKE_URL = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

# chrome broswer user-agent for http request
USER_AGENT = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'}

# data file to store history earhtquake record
DATA_FILE = "/home/pi/earthquake.his"

# recent eathquake time
RECENT_TIME = 3600 # one hour

def __read_latest_earthquake__():
    # read saved latest earthquake record
    file = None
    if os.path.exists(DATA_FILE):
        file = open(DATA_FILE, "r")
    else:
        file = open(DATA_FILE, "w+")
          
    try:
        earthquake = pickle.load(file)
    except:
        earthquake = None
    finally:
        file.close()
    
    return earthquake
    
def __save_latest_earthquake__(e):
    # save to history file
    file = open(DATA_FILE, "w")
    try:
        pickle.dump(e, file, pickle.HIGHEST_PROTOCOL)
    finally:
        file.close()
    
def __get_recent_earthquake__():
    earthquake = __read_latest_earthquake__()
    
    data = restget(EARTHQUAKE_URL, USER_AGENT)
    
    if data == "": return earthquake
    
    if data['metadata']['count'] > 0:
        feature = data['features'][0] # first record of earthquakes
        if feature["type"].upper() == "feature".upper() and (earthquake == None or feature['id'] != earthquake['id']):
            # get coordinate  and depth of earthquake
            coordinate = feature['geometry']['coordinates']
            lon = ("{:.2f} W".format(coordinate[0])) if coordinate[0] >= 0 else ("{:.2f} W".format(abs(coordinate[0])))
            lat = ("{:.2f} N".format(coordinate[1])) if coordinate[1] >= 0 else ("{:.2f} S".format(abs(coordinate[1])))
            depth = coordinate[2]
            
            earthquake = {"id": feature['id'],
                          "time": time.localtime(feature['properties']['time'] / 1000),
                          "place": feature['properties']["place"],
                          "mag": "Mag:{:.1f}".format(feature['properties']["mag"]),
                          "lat": "Lat:{:s}".format(lat),
                          "lon": "Lon:{:s}".format(lon),
                          "dep": "Dep:{:.1f} KM".format(depth)}
    
            __save_latest_earthquake__(earthquake)
            
    return earthquake
            
def show_earthquake():
    e = __get_recent_earthquake__()
    if e == None: return
    
    # if this earthquake is expired, older than two hours
    # not show
    if (time.time() - time.mktime(e['time'])) > RECENT_TIME: return
    
    lcd.display_words([chr(213) + chr(205) * 12 + chr(184),
                       chr(179) + " " * 12 + chr(179),
                       chr(179) + " EARTHQUAKE " + chr(179), 
                       chr(179) + "  in WORLD  " + chr(179),
                       chr(179) + " " * 12 + chr(179),
                       chr(212) + chr(205) * 12 + chr(190)])    
    time.sleep(4)
    
    lcd.alarm(3)
    lcd_ext.marquee_display_words([time.strftime("%m/%d %H:%M:%S", e['time']), e['place'], e['mag'], e['lat'], e['lon'], e['dep']], 1)
    lcd.alarm(3)
    time.sleep(2)
