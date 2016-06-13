import os
import picamera
import time
from time import strftime
import RPi.GPIO as GPIO
import datetime as dt

selection = 7                           # variable used for GPIO pin 7 "selection"
enable1 = 11                            # variable used for GPIO pin 11 "enable 1"
enable2 = 12                            # variable used for GPIO pin 12 "enable 2"

#camera = picamera.PiCamera()
#fname = 'test%s.txt' % strftime('_%H%M%S')
#fh = open(fname, 'w')
#fh.write('')
#fh.close()

GPIO.setmode(GPIO.BOARD)                # use board numbering scheme for GPIO header vs broadcom
GPIO.setup(selection, GPIO.OUT)
GPIO.setup(enable1, GPIO.OUT)
GPIO.setup(enable2, GPIO.OUT)

def enable_camera_A():
    GPIO.output(selection, False)
    GPIO.output(enable1, False)
    GPIO.output(enable2, True)
    camera.hflip = True
    camera.vflip = True
    camera.annotate_text = 'Camera A'

def enable_camera_B():
    GPIO.output(selection, True)
    GPIO.output(enable1, False)
    GPIO.output(enable2, True)
    camera.hflip = False
    camera.vflip = False
    camera.annotate_text = 'Camera B'

def enable_camera_C():
    GPIO.output(selection, False)
    GPIO.output(enable1, True)
    GPIO.output(enable2, False)
    camera.hflip = True
    camera.vflip = True
    camera.annotate_text = 'Camera C'

def enable_camera_D():
    GPIO.output(selection, True)
    GPIO.output(enable1, True)
    GPIO.output(enable2, False)
    camera.hflip = False
    camera.vflip = False
    camera.annotate_text = 'Camera D'

for x in range(0, 3):
    try:
        #camera.annotate_background = picamera.Color('black')
        camera = picamera.PiCamera()
        camera.resolution = (2592, 1944)
        # camera A
        enable_camera_A()
        time.sleep(2)
        name = 'CamA%s.png' % strftime('_%H_%M_%S')
        camera.capture(name)
        # camera B
        enable_camera_B()
        time.sleep(2)
        name = 'CamB%s.png' % strftime('_%H_%M_%S')
        camera.capture(name)
        # camera C
        enable_camera_C()
        time.sleep(2)
        name = 'CamC%s.png' % strftime('_%H_%M_%S')
        camera.capture(name)
        # camera D
        enable_camera_D()
        time.sleep(2)
        name = 'CamD%s.png' % strftime('_%H_%M_%S')
        camera.capture(name)
    except:
        #camera.close()
        #fh.open(fname, 'a')
        #fh.write('ERROR!! Hit exception in loop ' + str(x) + strftime(' %H_%M_%S\n'))
        #fh.close()
        GPIO.cleanup()
        os.system('sudo reboot')

    finally:
        #camera.stop_preview()
        camera.close()
        #fh = open(fname, 'a')
        #fh.write('Finished loop: ' + str(x) + strftime(' %H_%M_%S\n'))
        #fh.close()
        time.sleep(5)

GPIO.cleanup()
    
