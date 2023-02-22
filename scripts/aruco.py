#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv2 import aruco

def aruco_detect(image):

    # bridge converts the ROS image into CV2 image that can be used by the arUco library
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(image,desired_encoding='bgra8')

    gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    corners, ids, rejected = aruco.detectMarkers(gray_image,dictionary)
    # corners will have all the corners for the detected aruco tags

def __init__():
    rospy.init_node("aruco_detector")
    rospy.Subscriber("/camera", Image, aruco_detect)
    rospy.spin()

if __name__=="__main__":
    __init__()
