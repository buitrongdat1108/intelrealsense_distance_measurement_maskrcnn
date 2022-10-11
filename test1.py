import cv2
from realsense_camera import *

# Load Realsense camera
rs = RealsenseCamera()
while True:
    ret, bgr_frame, depth_frame = rs.get_frame_stream()
    point_x,point_y= 250,100
    distance_mm=depth_frame[point_y,point_x]
    cv2.circle(bgr_frame, (point_x, point_y), 8, (0,0,255), -1)
    cv2.putText(bgr_frame, "{}mm".format(distance_mm),(point_x, point_y-10),0,1,(0,0,255),2)
    cv2.imshow('bgr_frame', bgr_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break