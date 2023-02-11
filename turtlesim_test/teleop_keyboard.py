import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TeleopKeyboard(Node):
    def __init__(self):
        super().__init__("teleop_keyboard")
        self.publisher = self.create_publisher(Twist,"cmd_vel",10)
        self.timer = self.create_timer(0.01,self.timer_callback)
        self.vel = Twist()
        self.vel.linear.x = 0.0
        self.vel.angular.z = 0.0

    def timer_callback(self):
        key = input("u,j,m,k,hキー入力後にenter")
        if key == "u":
            self.vel.linear.x += 1.0
        elif key == "j":
            self.vel.linear.x = 0.0
            self.vel.angular.z = 0.0
        elif key == "m":
            self.vel.linear.x -= 1.0
        elif key == "k":
            self.vel.angular.z -= 1.0
        elif key == "h":
            self.vel.angular.z += 1.0
        
        self.publisher.publish(self.vel)
        self.get_logger().info(f"linear_x:{self.vel.linear.x},angular_z:{self.vel.angular.z}")


def main():
    rclpy.init()
    node = TeleopKeyboard()
    rclpy.spin(node)
    rclpy.shutdown()