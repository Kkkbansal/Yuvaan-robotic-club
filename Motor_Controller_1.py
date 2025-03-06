#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Int32MultiArray

def joy_callback(msg):
    x_axis = msg.axes[0]  # Assuming X axis of joystick
    y_axis = msg.axes[1]  # Assuming Y axis of joystick

    # Map joystick values to motor control commands
    motor_speed = [int(255 * x_axis), int(255 * y_axis)]  # Map [-1, 1] to [0, 255]

    # Create and publish motor control command
    motor_command = Int32MultiArray(data=motor_speed)
    motor_command_pub.publish(motor_command)

if __name__ == '__main__':
    rospy.init_node('motor_control_node')
    joy_sub = rospy.Subscriber('joy', Joy, joy_callback)
    motor_command_pub = rospy.Publisher('motor_command', Int32MultiArray, queue_size=10)
    rospy.spin()
