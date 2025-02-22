import wpilib
from wpilib import CameraServer

class Camera:
    def cameraInit():
        try:
            """Initialize camera"""
            cam1 = CameraServer.getInstance()
            cam1.enableLogging()
            cam1.startAutomaticCapture()
        except Exception as e:
            print(f"Something went wrong trying to initiate Camera: {e}")
