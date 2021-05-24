import picamera     # Importing the library for camera module
from time import sleep  # Importing sleep from time library to add delay in program
camera = picamera.PiCamera()    # Setting up the camera
camera.start_preview()      # You will see a preview window while recording
sleep(5)
camera.stop_preview()
camera.start_recording('/home/pi/Desktop/video.h264') # Video will be saved at desktop
sleep(60)
camera.stop_recording()
