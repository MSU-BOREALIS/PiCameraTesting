#! /bin/sh
import picamera
import time
from time import strftime
import datetime as dt

#camera = picamera.PiCamera()
with picamera.PiCamera() as camera:

    try:
        #with picamera.PiCamera() as camera:
        #camera.annotate_background = picamera.Color('black')
        camera.vflip = True
        camera.hflip = True
    
        #camera.start_preview()
        #time.sleep(2)

        for x in range (0, 20):
            camera.start_preview()
            time.sleep(2)
            camera.capture('%s.png' % strftime('%m%d_%H_%M_%S')) 
            time.sleep(1)
            camera.stop_preview()
            time.sleep(5)


    except:
        camera.close()

    finally:
        #camera.stop_preview()
        camera.close()

