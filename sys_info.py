#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import commands
import os
import sys
import pcd8544 as lcd
import sys_info_icon as icons


def __get_cpu_temp__():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp) / 1000

def __get_gpu_temp__():
    gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
    return float(gpu_temp)
    
def __get_mem_free__():
    mem_free = commands.getoutput( 'cat /proc/meminfo | grep MemFree | sed "s/[\ ,MemFree,kB,:]*//g"' )
    return float(mem_free) / 1024
    
def __get_cpu_idle__():
    cpu_idle = commands.getoutput( 'vmstat | tail -n1 | sed "s/\ \ */\ /g" | cut -d" " -f 16' )
    return 100 - int(cpu_idle)

def __get_network_rx__():
    network = commands.getoutput('vnstat -ru 0 -tr 2 | grep rx |cut -c -30|sed -e "s/\ //g" -e "s/rx/D:/g"')
    return network
    
def __get_network_tx__():
    network = commands.getoutput('vnstat -ru 0 -tr 2 | grep tx |cut -c -30|sed -e "s/\ //g" -e "s/tx/U:/g"')
    return network

def __get_disk_space__():
    p = os.popen("df -l -h /")
    i = 0
    while 1:
        i += 1
        line = p.readline()
        if i == 2:
            return(line.split()[1:5])

def __get_time__():
    return time.strftime("%m/%d %H:%M:%S", time.localtime())

    
def __draw_value__(value, x = 24, y = 0):
    for c in value:
        if c == ".":
            lcd.draw_bitmap(icons.POINT, x = x, y = y, w = 7, h = 24)
        else:
            lcd.draw_bitmap(icons.NUMBERS[ord(c) - ord("0")], x = x, y = y, w = 7, h = 24)
        x += 7
    
def show_sys_info():
    lcd.draw_bitmap(icons.SPLASH)
    time.sleep(5)
    
    for i in xrange(4):
        lcd.cls()
        # draw CPU and GPU icon and temp, usage
        lcd.draw_bitmap(icons.CPU, x = 3, w = 21, h = 24)
        __draw_value__("{:2.2f}".format(__get_cpu_temp__()), 27)
        lcd.draw_bitmap(icons.C_DEGREE, x = 66, w = 18, h = 24)
        
        lcd.draw_bitmap(icons.GPU, x = 3, y = 3, w = 21, h = 24)
        __draw_value__("{:2.2f}".format(__get_gpu_temp__()), 27, y = 3)    
        lcd.draw_bitmap(icons.C_DEGREE, x = 66, y = 3, w = 18, h = 24)
        time.sleep(2)
    
        lcd.cls()
        # CPU usage
        lcd.draw_bitmap(icons.CPU, x = 3, w = 21, h = 24)
        p = "{:d}".format(__get_cpu_idle__())
        __draw_value__(p, 55 - len(p) * 7)
        lcd.draw_bitmap(icons.PERCENTAGE, x = 67, w = 17, h = 24)
    
        # Memory usage
        lcd.draw_bitmap(icons.RAM, x = 3, y = 3, w = 21, h = 24)
        m = "{:.0f}".format(__get_mem_free__())
        __draw_value__(m, 55 - len(m) * 7, y = 3)
        lcd.draw_bitmap(icons.MB, x = 57, y = 3, w = 27, h = 24)
        time.sleep(2)
    
    lcd.display_words([__get_time__(), 
                      "----Net IO----",
                      "eth0:",
                      __get_network_rx__(),
                      __get_network_tx__(),
                      " " * 14])
    time.sleep(5)
    
    disk_stats = __get_disk_space__()
    lcd.display_words([__get_time__(),
                      "-----Disk-----",
                      "Used:" + disk_stats[1],
                      "Avail:" + disk_stats[2],
                      "Used%:" + disk_stats[3], 
                      " " * 14])
    time.sleep(5)
    
if __name__ == "__main__":
    lcd.init()
    lcd.light(1)
    show_sys_info()