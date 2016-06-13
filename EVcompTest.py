#  test program to iterate through camera settings

import picamera
import time              # needed for delay/sleep
import datetime as dt    # needed for dates, times, timestamp etc



camera = picamera.PiCamera()
camera.annotate_background = picamera.Color('black')
#settings = ''
camera.brightness = 50
camera.exposure_compensation = 0
#camera.exposure_mode = 'auto'

for x in range (0, 20):
    settings = 'Brightness: ' + str(camera.brightness) + ' EV comp: ' + str(camera.exposure_compensation)
    camera.annotate_text = settings
    time.sleep(5)
    camera.capture('imgtest%02d.png' %x)
    camera.brightness -= 2
    camera.exposure_compensation += 1
