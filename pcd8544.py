#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import ascii
import time
import sys

#gpio's :
SCLK = 16
DIN = 15
DC = 13
RST = 11
BG = 18

def init():
  GPIO.setwarnings(False)
  setup(0xbc)
  
def gotoxy(x, y):
  x = max(min(83, x), 0)
  y = max(min(5, y), 0)
  lcd_cmd(x+0x80)
  lcd_cmd(y+0x40)

def draw_bitmap(bits, x = 0, y = 0, w = 84, h = 48):
  gotoxy(x, y)
  for i in xrange(h // 8):
    for j in xrange(w):
        lcd_data(bits[i * w + j])
    gotoxy(x, y + 1 + i)
  gotoxy(0, 0)

def display_words(words, min_x = 0, max_x = 84, min_y = 0, max_y = 6):
  if words == None: return
  rows = max_y - min_y
  chrs = (max_x - min_x ) // 6
  line = min_y
  for word in words:
    if line > rows:
      cls(min_x, max_x, min_y, max_y)
      line = min_y
    gotoxy(min_x, line)
    display_word(' ' * chrs, min_x, line, chrs)
    gotoxy(min_x, line)
    display_word(word, min_x, line, chrs)
    line += len(word) // (chrs + 1) + 1
   
def display_word(word, x = 0, y = 0, chrs = 14):
  if word == None: return  
  chrs = min(14, max(0, chrs))
  gotoxy(x, y)
  for r in xrange(len(word) // (chrs + 1) + 1):
      for c in word[r * chrs: (r + 1) * chrs]:
        display_char(c)
      y += 1
      gotoxy(x, y)

def display_char(char):
  if ord(char) >= 0 and ord(char) <= 254:
    index = ord(char) * 5
    for i in xrange(5):
      lcd_data(ascii.chars[index+i])
    lcd_data(0) # space inbetween characters
  
def light(on):
  if on:
    GPIO.output(BG, True)
  else:
    GPIO.output(BG, False)

def alarm(t):
  for i in range(t):
    light(1)
    time.sleep(0.5)
    light(0)
    time.sleep(0.5)
    light(1)
    
def cls(min_x = 0, max_x = 84, min_y = 0, max_y = 6):
  gotoxy(min_x, min_y)
  for c in xrange(min_x, max_x):
    for r in xrange(min_y, max_y):
      lcd_data(0)  
  gotoxy(min_x, min_y)
      
def setup(contrast):
  # set pin directions
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(DIN, GPIO.OUT)
  GPIO.setup(SCLK, GPIO.OUT)
  GPIO.setup(DC, GPIO.OUT)
  GPIO.setup(RST, GPIO.OUT)
  GPIO.setup(BG, GPIO.OUT)
  time.sleep(1)
  
  # toggle RST low to reset
  GPIO.output(RST, False)
  time.sleep(0.1)
  GPIO.output(RST, True)
  lcd_cmd(0x21) # extended mode
  lcd_cmd(0x14) # bias
  lcd_cmd(contrast) # vop
  lcd_cmd(0x20) # basic mode
  lcd_cmd(0xc) # non-inverted display
  
  time.sleep(0.1)
  cls()
  
def spi(c):
  # data = DIN
  # clock = SCLK
  # MSB first
  # value = c
  for i in xrange(8):
    GPIO.output(DIN, (c & (1 << (7-i))) > 0)
    GPIO.output(SCLK, True)
    GPIO.output(SCLK, False)
    
def lcd_cmd(c):
  GPIO.output(DC, False)
  spi(c)
  
def lcd_data(c):
  GPIO.output(DC, True)
  spi(c)
