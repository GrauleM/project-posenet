import picamera     # Importing the library for camera module
from time import sleep  # Importing sleep from time library to add delay in program
camera = picamera.PiCamera(resolution = (1640, 1232), framerate=40)    # Setting up the camera
camera.rotation = 180
camera.start_preview()      # You will see a preview window while recording
print("start recording in 5s")
sleep(5)
print("start recording")
camera.start_recording('/home/pi/Desktop/video_1640x1232_40fps.h264', format='h264', level='4.2') # Video will be saved at desktop; level='4.2' is required for high framerate
for i in range(60):
    print(f"{i} seconds")
    sleep(1)
camera.stop_recording()
camera.stop_preview()
