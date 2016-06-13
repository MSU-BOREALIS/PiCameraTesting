import picamera
import time
import RPi.GPIO as GPIO
import datetime as dt

selection = 7                           # variable used for GPIO pin 7 "selection"
enable1 = 11                            # variable used for GPIO pin 11 "enable 1"
enable2 = 12                            # variable used for GPIO pin 12 "enable 2"

#camera = picamera.PiCamera()

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

    #camera.annotate_background = picamera.Color('black')
#time.sleep(1200)

for x in range(0, 50):
    try:
        camera = picamera.PiCamera()
        # camera A
        enable_camera_A()
        time.sleep(1)
        camera.start_preview()
        time.sleep(2)
        camera.capture('camA%02d.png' %x)
        camera.stop_preview()
        # camera B
        enable_camera_B()
        time.sleep(1)
        camera.start_preview()
        time.sleep(2)
        camera.capture('camB%02d.png' %x)
        camera.stop_preview()
        # camera C
        enable_camera_C()
        time.sleep(1)
        camera.start_preview()
        time.sleep(2)
        camera.capture('camC%02d.png' %x)
        camera.stop_preview()
        # camera D
        enable_camera_D()
        time.sleep(1)
        camera.start_preview()
        time.sleep(2)
        camera.capture('camD%02d.png' %x)
        camera.stop_preview()
       
    finally:
        #camera.stop_preview()
        camera.close()
        time.sleep(3)

GPIO.cleanup()
    
