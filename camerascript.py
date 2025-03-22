import cv2
import numpy as np
from cscore import CameraServer as CS
from pupil_apriltags import Detector
import time

def main():
    # Enable logging and start capture
    CS.enableLogging()
    cam1 = CS.startAutomaticCapture()
    cam1.setResolution(640, 480)

    cvSink = CS.getVideo()
    outputStream = CS.putVideo("cam1", 640, 480)

    # Preallocate image
    mat = np.zeros(shape=(480, 640, 3), dtype=np.uint8)

    # Initialize the AprilTag detector
    # Adjust parameters (families, quad_decimate, etc.) as needed.
    at_detector = Detector(
        families="tag36h11",
        nthreads=4,
        quad_decimate=1.0,
        quad_sigma=0.0,
        refine_edges=1,
        decode_sharpening=0.25,
        debug=0
    )

    # Load camera calibration parameters if available
    camera_params = [600, 600, 320, 240]
    tag_size = 0.166  # Example: Tag size in meters

    while True:
        timestamp, mat = cvSink.grabFrame(mat)
        if timestamp == 0:
            outputStream.notifyError(cvSink.getError())
            continue

        # Convert frame to grayscale for detection
        gray = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)

        # Run AprilTag detection
        tags = at_detector.detect(
            gray,
            estimate_tag_pose=True,
            camera_params=camera_params,
            tag_size=tag_size
        )

        # Process detected tags
        for tag in tags:
            # Print tag id and pose estimation
            print(f"Detected tag {tag.tag_id} at pose: {tag.pose_R}, {tag.pose_t}")
            
            # Optionally, draw a rectangle around the detected tag
            pts = tag.corners.reshape((-1,1,2)).astype(np.int32)
            cv2.polylines(mat, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
            
            # Use tag.pose_t (translation vector) to compute distance and angle
            # This information can then be used to control your robot.
            # For instance, you might adjust the drivetrain command based on the tag's position.

        # Display output (if desired) and push frame to output stream
        outputStream.putFrame(mat)

if __name__ == "__main__":
    main()
