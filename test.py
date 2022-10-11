import cv2
from realsense_camera import *

# Load Realsense camera
rs = RealsenseCamera()
while True:
    ret, bgr_frame, depth_frame = rs.get_frame_stream()
    cv2.imshow('bgr_frame', bgr_frame)
    print(depth_frame)
    cv2.imshow('depth_frame', depth_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


