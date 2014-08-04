#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import commands
import os
import sys

def __get_cpu_temp__():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return "CPU:{0:2.2f} {1:s}C".format(float(cpu_temp)/1000, chr(167))

def __get_gpu_temp__():
    gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
    return "GPU:{0:2.2f} {1:s}C".format(float(gpu_temp), chr(167))
    
def __get_mem_free__():
    mem_free = commands.getoutput( 'cat /proc/meminfo | grep MemFree | sed "s/[\ ,MemFree,kB,:]*//g"' )
    return "MemF:{:.2f}MB".format(float(mem_free)/1024)
    
def __get_cpu_idle__():
    cpu_idle = commands.getoutput( 'vmstat | tail -n1 | sed "s/\ \ */\ /g" | cut -d" " -f 16' )
    return "CPU U:{:d}%".format(100 - int(cpu_idle))

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

def show_sys_info(call):
    for i in xrange(5):
        call([__get_time__(), 
              "---Sys Info---",
              __get_cpu_temp__(),
              __get_gpu_temp__(),
              __get_mem_free__(),
              __get_cpu_idle__()])
        time.sleep(1)
    
    call([__get_time__(), 
          "----Net IO----",
          "eth0:",
          __get_network_rx__(),
          __get_network_tx__(),
          " "*14])
    time.sleep(5)
    
    disk_stats = __get_disk_space__()
    call([__get_time__(),
          "-----Disk-----",
          "Used:"+disk_stats[1],
          "Avail:"+disk_stats[2],
          "Used%:"+disk_stats[3], 
          " "*14])
    time.sleep(5)
