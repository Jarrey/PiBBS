#!/usr/bin/python
# -*- coding: utf-8 -*-

NUM_0 = [
0x00, 0x00, 0x80, 0x80, 0x80, 0x80, 0x00, 0x00, 0xFE, 0xFF, 0x01, 0x01, 0xFF, 0xFE, 0x00, 0x00,
0x03, 0x03, 0x03, 0x03, 0x00, 
]

NUM_1 = [
0x00, 0x00, 0x00, 0x00, 0x80, 0x80, 0x00, 0x00, 0x00, 0x0C, 0x06, 0xFF, 0xFF, 0x00, 0x00, 0x00,
0x00, 0x00, 0x03, 0x03, 0x00, 
]

NUM_2 = [
0x00, 0x00, 0x00, 0x80, 0x80, 0x80, 0x00, 0x00, 0x06, 0xC7, 0xE1, 0x71, 0x3F, 0x0F, 0x00, 0x03,
0x03, 0x03, 0x03, 0x03, 0x03, 
]

NUM_3 = [
0x00, 0x00, 0x80, 0x80, 0x80, 0x80, 0x00, 0x00, 0x83, 0x83, 0x19, 0x19, 0xFF, 0xE7, 0x00, 0x01,
0x03, 0x03, 0x03, 0x03, 0x00, 
]

NUM_4 = [
0x00, 0x00, 0x00, 0x00, 0x80, 0x80, 0x00, 0xE0, 0xF0, 0xDC, 0xC7, 0xFF, 0xFF, 0xC0, 0x00, 0x00,
0x00, 0x00, 0x03, 0x03, 0x00, 
]

NUM_5 = [
0x00, 0x00, 0x80, 0x80, 0x80, 0x80, 0x80, 0x00, 0xDC, 0xDF, 0x0B, 0x0D, 0xFD, 0xF9, 0x00, 0x00,
0x03, 0x03, 0x03, 0x03, 0x00, 
]

NUM_6 = [
0x00, 0x00, 0x80, 0x80, 0x80, 0x00, 0x00, 0x00, 0xFE, 0xFF, 0x19, 0xFB, 0xF3, 0x00, 0x00, 0x00,
0x03, 0x03, 0x03, 0x01, 0x00, 
]

NUM_7 = [
0x00, 0x80, 0x80, 0x80, 0x80, 0x80, 0x00, 0x00, 0x01, 0xC1, 0xF9, 0x1F, 0x03, 0x00, 0x00, 0x00,
0x03, 0x03, 0x00, 0x00, 0x00, 
]

NUM_8 = [
0x00, 0x00, 0x80, 0x80, 0x80, 0x80, 0x00, 0x00, 0xE7, 0xFF, 0x19, 0x19, 0xFF, 0xE7, 0x00, 0x01,
0x03, 0x03, 0x03, 0x03, 0x01, 
]

NUM_9 = [
0x00, 0x00, 0x80, 0x80, 0x80, 0x00, 0x00, 0x00, 0x9F, 0xBF, 0x31, 0x31, 0xFF, 0xFE, 0x00, 0x01,
0x03, 0x03, 0x03, 0x01, 0x00, 
]

NUMBERS = [NUM_0, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, NUM_7, NUM_8, NUM_9]

C_DEGREE = [
0x00, 0x40, 0xA0, 0x40, 0x00, 0x00, 0x80, 0xC0, 0xE0, 0x60, 0x60, 0x60, 0xE0, 0xC0, 0x80, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x7E, 0xFF, 0x81, 0x00, 0x00, 0x00, 0x00, 0x00, 0x81,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x03, 0x07, 0x06, 0x06, 0x06,
0x07, 0x03, 0x01, 0x00, 0x00, 0x00, 
]

CPU = [
0x00, 0x00, 0x00, 0x00, 0xC0, 0xC0, 0xD8, 0xC0, 0xD8, 0xC0, 0xD8, 0xC0, 0xD8, 0xC0, 0xD8, 0xC0,
0xC0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x55, 0x55, 0x00, 0xFF, 0xE7, 0xDB, 0xDB, 0xFF, 0xC3, 0xEB,
0xF7, 0xFF, 0xE3, 0xDF, 0xE3, 0xFF, 0x00, 0x55, 0x55, 0x00, 0x00, 0x01, 0x01, 0x00, 0x07, 0x07,
0x37, 0x07, 0x37, 0x07, 0x37, 0x07, 0x37, 0x07, 0x37, 0x07, 0x07, 0x00, 0x01, 0x01, 0x00, 
]

GPU = [
0x00, 0x00, 0x00, 0x00, 0xC0, 0xC0, 0xD8, 0xC0, 0xD8, 0xC0, 0xD8, 0xC0, 0xD8, 0xC0, 0xD8, 0xC0,
0xC0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x55, 0x55, 0x00, 0xFF, 0xE7, 0xDB, 0xCB, 0xFF, 0xC3, 0xEB,
0xF7, 0xFF, 0xE3, 0xDF, 0xE3, 0xFF, 0x00, 0x55, 0x55, 0x00, 0x00, 0x01, 0x01, 0x00, 0x07, 0x07,
0x37, 0x07, 0x37, 0x07, 0x37, 0x07, 0x37, 0x07, 0x37, 0x07, 0x07, 0x00, 0x01, 0x01, 0x00, 
]

MB = [
0x00, 0x00, 0xE0, 0xE0, 0xE0, 0xE0, 0x00, 0x00, 0x00, 0xC0, 0xE0, 0xE0, 0xE0, 0x00, 0x00, 0xE0,
0xE0, 0x60, 0x60, 0x60, 0x60, 0x60, 0xC0, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0x01,
0x3F, 0xF8, 0x00, 0xF8, 0x3F, 0x01, 0xFF, 0xFF, 0x00, 0x00, 0xFF, 0xFF, 0x18, 0x18, 0x18, 0x18,
0x3C, 0xFF, 0xE7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x07, 0x00, 0x00, 0x07, 0x07, 0x07, 0x00,
0x00, 0x07, 0x07, 0x00, 0x00, 0x07, 0x07, 0x06, 0x06, 0x06, 0x06, 0x06, 0x03, 0x01, 0x00, 0x00,
0x00, 
]

PERCENTAGE = [
0x00, 0x00, 0xC0, 0xE0, 0x20, 0xE0, 0xC0, 0x00, 0x00, 0x80, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x07, 0x0F, 0x08, 0x0F, 0xC7, 0x30, 0x0C, 0xE3, 0xF0, 0x10, 0xF0, 0xE0, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0x01, 0x00, 0x00, 0x03, 0x07, 0x04, 0x07, 0x03,
0x00, 0x00, 0x00, 
]

POINT = [
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x03, 0x03, 0x00, 0x00, 
]

RAM = [
0x00, 0x80, 0x80, 0xB8, 0x80, 0xB8, 0x80, 0xB8, 0x80, 0xB8, 0x80, 0xB8, 0x80, 0xB8, 0x80, 0xB8,
0x80, 0xB8, 0x80, 0x80, 0x00, 0x00, 0xFF, 0xFF, 0xC7, 0xEB, 0xEB, 0xD7, 0xFF, 0xC7, 0xEB, 0xEB,
0xC7, 0xFF, 0xC7, 0xFB, 0xC3, 0xFB, 0xC7, 0xFF, 0xFF, 0x00, 0x00, 0x03, 0x03, 0x3B, 0x03, 0x3B,
0x03, 0x3B, 0x03, 0x3B, 0x03, 0x3B, 0x03, 0x3B, 0x03, 0x3B, 0x03, 0x3B, 0x03, 0x03, 0x00, 
]

SPLASH = [
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x38, 0x7C, 0x64, 0xE4,
0xC8, 0x00, 0x70, 0xF0, 0x00, 0xF0, 0x70, 0x00, 0x60, 0xF0, 0xD0, 0x90, 0x10, 0xF8, 0xF8, 0x10,
0x00, 0xE0, 0xF0, 0x50, 0x70, 0x60, 0x00, 0xF0, 0xF0, 0x10, 0xF0, 0xE0, 0x10, 0xF0, 0xE0, 0x00,
0x00, 0x00, 0x00, 0x00, 0xFC, 0xFC, 0x00, 0xF0, 0xF0, 0x10, 0xF0, 0xE0, 0x10, 0xF8, 0xFC, 0x14,
0x00, 0xE0, 0xF0, 0x10, 0xF0, 0xE0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xC0, 0xC0,
0x01, 0x02, 0xC2, 0xC3, 0x01, 0x00, 0xC0, 0xCD, 0x0F, 0x03, 0xC0, 0xC0, 0x02, 0x02, 0xC3, 0xC1,
0x00, 0x01, 0xC3, 0xC2, 0x00, 0x01, 0x03, 0x02, 0x02, 0x02, 0x00, 0x03, 0x03, 0x00, 0x03, 0x03,
0x00, 0x03, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x83, 0x80, 0x03, 0x03, 0x80, 0x83, 0x03,
0x00, 0x83, 0x83, 0x00, 0x00, 0x81, 0x83, 0x02, 0x03, 0x81, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xC0,
0xC0, 0xC0, 0xCF, 0xCF, 0xC0, 0xC0, 0xCF, 0xCF, 0xC0, 0xC0, 0xCF, 0xCF, 0xC0, 0xC0, 0xCF, 0xCF,
0xC0, 0xC0, 0xCF, 0xCF, 0xC0, 0xC0, 0xCF, 0xCF, 0xC0, 0xC0, 0xC0, 0x80, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x60, 0x60, 0x60, 0x60, 0x00, 0x00, 0xE7, 0xE7, 0xE0,
0xE0, 0xE7, 0xE7, 0xE0, 0xE0, 0xE7, 0xE7, 0xE0, 0xE0, 0xE7, 0xE7, 0xE0, 0xE0, 0xE7, 0xE7, 0x00,
0x00, 0x60, 0x60, 0x60, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0xFF, 0xFF, 0x07, 0x03, 0xB3, 0x33, 0x03, 0xC7, 0xFF, 0xFF, 0x07, 0x03, 0x33, 0x33,
0x03, 0x07, 0xFF, 0xFF, 0x07, 0x03, 0xF3, 0xF3, 0x03, 0x03, 0xF3, 0xF3, 0x03, 0x07, 0xFF, 0xFF,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x66, 0x66, 0x66, 0x66, 0x00,
0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x66, 0x66, 0x66, 0x66, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1F, 0x3F, 0x3E, 0x3E, 0x3F, 0x3F, 0x3E, 0x3E, 0x3F, 0x3F,
0x3E, 0x3E, 0x3F, 0x3F, 0x3E, 0x3E, 0x3F, 0x3F, 0x3E, 0x3E, 0x3F, 0x3F, 0x3E, 0x3E, 0x3F, 0x3F,
0x3E, 0x3E, 0x3F, 0x1F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x66,
0x66, 0x66, 0x66, 0x00, 0x00, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F,
0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x7F, 0x00, 0x00, 0x66, 0x66, 0x66, 0x66, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3F, 0x3F,
0x00, 0x00, 0x3F, 0x3F, 0x00, 0x00, 0x3F, 0x3F, 0x00, 0x00, 0x3F, 0x3F, 0x00, 0x00, 0x3F, 0x3F,
0x00, 0x00, 0x3F, 0x3F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x1E, 0x00, 0x00, 0x1E, 0x1E, 0x00,
0x00, 0x1E, 0x1E, 0x00, 0x00, 0x1E, 0x1E, 0x00, 0x00, 0x1E, 0x1E, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
]