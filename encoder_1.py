#!/usr/bin/env python3

import rospy
# from std_msgs.msg import Int32
from my_pkg.msg import my_msg

def encoder_callback(data):
    rospy.loginfo("Encoder values: %d, %d, %d, %d" % (data.points[0], data.points[1], data.points[2], data.points[3]))
    my_array = data.points

    # Add your control logic here

def listener():
    rospy.init_node('encoder_listener', anonymous=True)
    rospy.Subscriber("encoder", my_msg, encoder_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass