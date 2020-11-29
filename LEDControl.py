# UAS Pilot Data Collection Tool
# CSCE 483 - Texas A&M University Fall 2020
# Christopher Wray, Jordan Griffin, Samuel Sells, Venkata Dubagunta
# This code was created for our senior design project intended for UAS Pilot Researchers
# Code was inherited from Spring 2020 Team : Rahul Rana, Aranpreet Gill, Maria Tyas, Juan Minor, Adolfo Herrera
# Previous team version available at : https://github.com/AparnaDubagunta98/UAS-PILOT-DATA-COLLECTION/tree/master/LEGACY

#LED Functions

# Imports
import board
import neopixel

#constants for different colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# Connect to the LED on GPIO Pin 18
LED = neopixel.NeoPixel(board.D18, 1)

#turn LED Red
def turnRed():
    LED[0] = red
    return

#turn LED Green
def turnGreen():
    LED[0] = green
    return

#turn LED Blue
def turnBlue():
    LED[0] = blue
    return

def turnOrange():
    LED[0] = (255, 165, 0)
    return

#turn LED a custom color (r,g,b)
def turnCustom(r, g, b):
    if(r < 0 or r > 255):
        r = 0
    if(g < 0 or g > 255):
        g = 0
    if(b < 0 or b > 255):
        b = 0
    LED[0] = (r,g,b)
    return
