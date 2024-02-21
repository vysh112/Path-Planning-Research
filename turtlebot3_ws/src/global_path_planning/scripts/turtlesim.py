#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class MoveTurtleNode:
    def __init__(self):
        # Initialize the ROS Node
        rospy.init_node('move_turtle_node', anonymous=True)

        # Subscribe to the cmd_vel topic
        rospy.Subscriber('/cmd_vel', Twist, self.cmd_vel_callback)

        # Initialize the publisher for turtle movement
        self.turtle_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        # Rate at which to publish messages
        self.rate = rospy.Rate(10)

        # Start the main loop
        self.main_loop()

    def cmd_vel_callback(self, data):
        # Callback function for cmd_vel topic
        rospy.loginfo("Received cmd_vel: Linear - {}, Angular - {}".format(data.linear.x, data.angular.z))

        # Publish the received Twist message to control the turtle
        self.turtle_pub.publish(data)

    def main_loop(self):
        # Main loop to keep the node running
        while not rospy.is_shutdown():
            self.rate.sleep()

if __name__ == '__main__':
    try:
        # Create an instance of the MoveTurtleNode class
        move_turtle_node = MoveTurtleNode()
    except rospy.ROSInterruptException:
        pass
