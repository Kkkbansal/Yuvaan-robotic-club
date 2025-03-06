import rospy
from std_msgs.msg import Int32, Float32
from geometry_msgs.msg import Twist

speed_result = None
def depth_callback(msg_1):
    global speed_result
    x = 2
    twist_1 = Twist()
    if msg_1.data > x:
        if speed_result is not None:
            rospy.loginfo(speed_result)
            autonomus_pub.publish(speed_result)
    else:
        twist_1.linear.x = -0.5
        autonomus_pub.publish(twist_1)
    rate.sleep()

def speed_callback(msg_2):
    global speed_result
    twist_2 = Twist()
    # left
    if msg_2.data == -1:
        twist_2.linear.x = 0.1  # Linear velocity in x direction
        twist_2.angular.z = 0.5  # Angular velocity around z axis
    # right
    elif msg_2.data == 1:
        twist_2.linear.x = 0.1  # Linear velocity in x direction
        twist_2.angular.z = -0.5  # Angular velocity around z axis
    # straight
    elif msg_2.data == 0:
        twist_2.linear.x = 0.9  # Linear velocity in x direction
    speed_result = twist_2
    
if __name__ == '__main__':
    rospy.init_node('autonomus')
    rate = rospy.Rate(10)  # 10 Hz
    rospy.Subscriber('camera_int', Int32, speed_callback)
    rospy.Subscriber('camera_float', Float32, depth_callback)
    autonomus_pub = rospy.Publisher('motor_command', Twist, queue_size=10)
    rospy.spin()
