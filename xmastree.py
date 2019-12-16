#!/usr/bin/python
#
import sys, time, lockfile, datetime
import daemon

from neopixel import *


# LED strip configuration:
LED_COUNT      = 100     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 6       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def animate(strip,wait):
    for j in range(256):
       for i in range(strip.numPixels()):
          strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
       strip.show()
       time.sleep(wait)

def off(strip):
     for i in range(strip.numPixels()):
         strip.setPixelColor(i, Color(0,0,0) )
     strip.show()

def blinky(strip,wait):
   while True:
      now = datetime.datetime.now()

      if now.hour < 7:
          off(strip)
          time.sleep(10)
      else:
          animate(strip,wait)

blinky(strip,20.0/1000.0)

