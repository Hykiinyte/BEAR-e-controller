import numpy as np
from cscore import CameraServer as CS



def main():
    CS.enableLogging()

    cam1 = CS.startAutomaticCapture()
    cam1.setResolution(640, 480)

    cvSink = CS.getVideo()
    outputStream = CS.putVideo("cam1", 640, 480)

    # Allocating new images is very expensive, always try to preallocate
    mat = np.zeros(shape=(480, 640, 3), dtype=np.uint8)

    while True:
        # Tell the CvSink to grab a frame from the camera and put it
        # in the source image.  If there is an error notify the output.
        time, mat = cvSink.grabFrame(mat)
        if time == 0:
            outputStream.notifyError(cvSink.getError())
            continue

        outputStream.putFrame(mat)
