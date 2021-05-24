import picamera     # Importing the library for camera module
from time import sleep  # Importing sleep from time library to add delay in program
camera = picamera.PiCamera()    # Setting up the camera
camera.start_preview()      # You will see a preview window while recording
print("start recording in 5s")
sleep(5)
print("start recording in 5s")
camera.start_recording('/home/pi/Desktop/video.h264') # Video will be saved at desktop
for i in range(60):
    print(f"{i} seconds")
    sleep(1)
camera.stop_recording()
camera.stop_preview()
