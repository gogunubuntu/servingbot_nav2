# Basic ROS 2 program to subscribe to real-time streaming
# video from your built-in webcam
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com

# Import the necessary libraries
from email.mime import image
from re import I
from time import sleep
import random
import rclpy  # Python library for ROS 2
from rclpy.node import Node  # Handles the creation of nodes
from geometry_msgs.msg import Twist

class Stopper(Node):
    """
    Create an ImageSubscriber class, which is a subclass of the Node class.
    """

    def __init__(self):
        super().__init__(f"Stopper")
        self.pub_cmd_vel = self.create_publisher(Twist, "cmd_vel", 10)
        zero_vel = Twist()
        zero_vel.linear.x = 0.0
        zero_vel.angular.z = 0.0

        try:
            while True: sleep(.1)
        except KeyboardInterrupt:
            for i in range(200):
                try:
                    self.pub_cmd_vel.publish(zero_vel)
                    self.get_logger().info("publish zero velocity for safety!")
                    sleep(0.05)
                except KeyboardInterrupt: pass
def main():
    rclpy.init()
    node = Stopper()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
