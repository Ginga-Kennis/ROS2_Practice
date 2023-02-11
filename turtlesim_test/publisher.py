import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Publisher(Node):
    def __init__(self):
        super().__init__('publisher')
        self.pub = self.create_publisher(String,'Message',10)
        self.timer = self.create_timer(1.0,self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f"Hello {self.i}"
        self.pub.publish(msg)
        self.get_logger().info(msg.data)
        self.i += 1


def main():
    rclpy.init()
    node = Publisher()
    rclpy.spin(node)
    rclpy.shutdown()

