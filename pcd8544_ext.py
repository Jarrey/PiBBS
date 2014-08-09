#!/usr/bin/python
# -*- coding: utf-8 -*-

import pcd8544 as lcd
import time

def alarm_display_words(words, min_x = 0, max_x = 84, min_y = 0, max_y = 6):
    if words == None: return
    lcd.alarm(1)
    lcd.display_words(words, min_x, max_x, min_y, max_y)

def marquee_display_words(words, index = 0, min_x = 0, max_x = 84, min_y = 0, max_y = 6, alarm = 0):
    if words == None: return
    if index < 0 or index >= len(words): index = 0
    
    txt = words[index]
    if len(txt) <= 14:
        lcd.display_words(words, min_x, max_x, min_y, max_y)
    else:
        for t in xrange(max(2, 30//(len(txt)-13))):
            for i in xrange(len(txt)-13):
                copy_words = words[:]
                copy_words[index] = txt[i:i+14]
                lcd.display_words(copy_words, min_x, max_x, min_y, max_y)
                time.sleep(.2)
            time.sleep(2)

def shake_display_words(words, index = 0, times = 3, min_x = 0, max_x = 84, min_y = 0, max_y = 6):
    if words == None: return
    if index < 0 or index >= len(words): index = 0
    
    cnt_space_char = 0
    txt = words[index]
    chrs = (max_x - min_x) // 6
    max_space = chrs - len(txt)
    
    for i in xrange((max_space + 1) * times):
        if cnt_space_char > max_space:
            cnt_space_char = 0
            
        copy_words = words[:]
        copy_words[index] = (' ' * cnt_space_char + txt).ljust(chrs)
        lcd.display_words(copy_words, min_x, max_x, min_y, max_y)
        cnt_space_char += 1
        time.sleep(.3)