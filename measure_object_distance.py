import cv2
from realsense_camera import *
from mask_rcnn import *

# Load Realsense camera
rs = RealsenseCamera()
mrcnn = MaskRCNN()

# write flask function from here
while True:
    # Get frame in real time from Realsense camera
    ret, bgr_frame, depth_frame = rs.get_frame_stream()

    # Get object mask
    boxes, classes, contours, centers = mrcnn.detect_objects_mask(bgr_frame)

    # box=boxes[0,0,i],(x,y,x2,y2)=(box[3] * width,box[4]*height,box[5]*width,box[6]*height), box is only the ratio of the frames
    # class_index= box[1], confidence=box[2]

    # Draw object mask
    bgr_frame = mrcnn.draw_object_mask(bgr_frame)

    # Show depth info of the objects
    mrcnn.draw_object_info(bgr_frame, depth_frame)

    cv2.imshow("depth frame", depth_frame)
    cv2.imshow("Bgr frame", bgr_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

rs.release()
cv2.destroyAllWindows()