#! /bin/sh
import picamera
import time
import datetime as dt

camera = picamera.PiCamera()

try:
    #camera.annotate_background = picamera.Color('black')
    camera.vflip = True
    camera.hflip = True
    
    camera.start_preview()
    time.sleep(2)

    for x in range (0, 10):
        camera.capture('%s.png' % strftime('%m%d_%H_%M_%S')) 
        time.sleep(2)


except:
    camera.close()

finally:
    camera.stop_preview()
    camera.close()
    
