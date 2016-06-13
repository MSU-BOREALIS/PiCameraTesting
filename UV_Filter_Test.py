#! bin/sh
# ---------------------------------------------------------------
#
#              UV_Filter_Test
#
#   Python 2.7 script used in conjuction with
#   four pi cameras and camera mux used to test
#   three different UV filters
#   "CameraA" port = kodak 2B filter
#   "CameraB" port = kodak 2A filter
#   "CameraC" port = no filter (control)
#   "CameraD" port = kodak 2E filter
#
#    Author: David Schwehr    Montana Space Grant / BOREALIS
#
# ----------------------------------------------------------------

import picamera
import time
from time import strftime
import RPi.GPIO as GPIO
import datetime as dt

selection = 7                           # variable used for GPIO pin 7 "selection"
enable1 = 11                            # variable used for GPIO pin 11 "enable 1"
enable2 = 12                            # variable used for GPIO pin 12 "enable 2"

#camera = picamera.PiCamera()
fname = 'settings%s.txt' % strftime('%m%Y_%H%M%S')
fh = open(fname, 'w')
fh.write('')
fh.close()

GPIO.setmode(GPIO.BOARD)                # use board numbering scheme for GPIO header vs broadcom
GPIO.setup(selection, GPIO.OUT)
GPIO.setup(enable1, GPIO.OUT)
GPIO.setup(enable2, GPIO.OUT)

def enable_camera_A():                  # enable camera on port with 'camera A ' in silkscreen
    GPIO.output(selection, False)
    GPIO.output(enable1, False)
    GPIO.output(enable2, True)
    camera.hflip = True
    camera.vflip = True
    #camera.annotate_text = 'Camera A'

def enable_camera_B():                  # enable camera on port with 'camera B' in silkscreen
    GPIO.output(selection, True)
    GPIO.output(enable1, False)
    GPIO.output(enable2, True)
    camera.hflip = False
    camera.vflip = False
    #camera.annotate_text = 'Camera B'

def enable_camera_C():                  # enable camera on port wtih 'camera C' in silkscreen
    GPIO.output(selection, False)
    GPIO.output(enable1, True)
    GPIO.output(enable2, False)
    camera.hflip = True
    camera.vflip = True
    #camera.annotate_text = 'Camera C'

def enable_camera_D():                  # enable camera on port with 'Camera D' in silkscreen
    GPIO.output(selection, True)
    GPIO.output(enable1, True)
    GPIO.output(enable2, False)
    camera.hflip = False
    camera.vflip = False
    #camera.annotate_text = 'Camera D'

    #camera.annotate_background = picamera.Color('black')   # may not be using annotations for balloon flight
time.sleep(1200)

for x in range(0, 100):                                  # may use nested loop for defualt camera settings and changing camera settings
    try:
        camera = picamera.PiCamera()
        camera.resolution = (2592,1944)
        # camera A
        enable_camera_A()
        #camera.start_preview()                             # need to use a delay/sleep or preview to give each camera time to adjust auto settings or turn off AWB
        time.sleep(2)
        name = 'camA%s.png' % strftime('%m%d%Y_%H_%M_%S')
        camera.capture(name)
        settings = name + '                        Bright: ' + str(camera.brightness) + ' Contrast: ' + str(camera.contrast) + ' Saturation: ' + str(camera.saturation) + ' Sharpness: ' + str(camera.sharpness) + ' ISO: ' + str(camera.ISO)
        fh = open(fname, 'a')
        fh.write(settings + '\n')
        fh.close()
        name = '/usr/local/bin/uv_test/camA%s.png' % strftime('%m%d%Y_%H_%M_%S')
        camera.capture(name)
        settings = name + ' Bright: ' + str(camera.brightness) + ' Contrast: ' + str(camera.contrast) + ' Saturation: ' + str(camera.saturation) + ' Sharpness: ' + str(camera.sharpness) + ' ISO: ' + str(camera.ISO)
        fh = open(fname, 'a')
        fh.write(settings + '\n')
        fh.close()
        # camera B
        enable_camera_B()
        time.sleep(2)
        name = 'camB%s.png' % strftime('%m%d%Y_%H_%M_%S')
        camera.capture(name)
        settings = name + '                        Bright: ' + str(camera.brightness) + ' Contrast: ' + str(camera.contrast) + ' Saturation: ' + str(camera.saturation) + ' Sharpness: ' + str(camera.sharpness) + ' ISO: ' + str(camera.ISO)
        fh = open(fname, 'a')
        fh.write(settings + '\n')
        fh.close()
        name = '/usr/local/bin/uv_test/camB%s.png' % strftime('%m%d%Y_%H_%M_%S')
        camera.capture(name)
        settings = name + ' Bright: ' + str(camera.brightness) + ' Contrast: ' + str(camera.contrast) + ' Saturation: ' + str(camera.saturation) + ' Sharpness: ' + str(camera.sharpness) + ' ISO: ' + str(camera.ISO)
        fh = open(fname, 'a')
        fh.write(settings + '\n')
        fh.close()
        # camera C
        enable_camera_C()
        time.sleep(2)
        name = 'camC%s.png' % strftime('%m%d%Y_%H_%M_%S')
        camera.capture(name)
        settings = name + '                        Bright: ' + str(camera.brightness) + ' Contrast: ' + str(camera.contrast) + ' Saturation: ' + str(camera.saturation) + ' Sharpness: ' + str(camera.sharpness) + ' ISO: ' + str(camera.ISO)
        fh = open(fname, 'a')
        fh.write(settings + '\n')
        fh.close()
        name = '/usr/local/bin/uv_test/camC%s.png' % strftime('%m%d%Y_%H_%M_%S')
        camera.capture(name)
        settings = name + ' Bright: ' + str(camera.brightness) + ' Contrast: ' + str(camera.contrast) + ' Saturation: ' + str(camera.saturation) + ' Sharpness: ' + str(camera.sharpness) + ' ISO: ' + str(camera.ISO)
        fh = open(fname, 'a')
        fh.write(settings + '\n')
        fh.close()
        # camera D
        enable_camera_D()
        time.sleep(2)
        name = 'camD%s.png' % strftime('%m%d%Y_%H_%M_%S')
        camera.capture(name)
        settings = name + '                        Bright: ' + str(camera.brightness) + ' Contrast: ' + str(camera.contrast) + ' Saturation: ' + str(camera.saturation) + ' Sharpness: ' + str(camera.sharpness) + ' ISO: ' + str(camera.ISO)
        fh = open(fname, 'a')
        fh.write(settings + '\n')
        fh.close()
        name = '/usr/local/bin/uv_test/camD%s.png' % strftime('%m%d%Y_%H_%M_%S')
        camera.capture(name)
        settings = name + ' Bright: ' + str(camera.brightness) + ' Contrast: ' + str(camera.contrast) + ' Saturation: ' + str(camera.saturation) + ' Sharpness: ' + str(camera.sharpness) + ' ISO: ' + str(camera.ISO)
        fh = open(fname, 'a')
        fh.write(settings + '\n')
        fh.close()
    except:
        camera.close()
        GPIO.cleanup()

    finally:
        #camera.stop_preview()
        camera.close()
        time.sleep(60)
GPIO.cleanup()

