import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubPub(Node):
    def __init__(self):
        super().__init__('subpub')
        self.pub = self.create_publisher(String,'Topic',10)
        self.sub = self.create_subscription(String,'Message',self.callback,10)
        self.timer = self.create_timer(0.1,self.timer_callback)
        self.i = 0

    def callback(self,msg):
        self.get_logger().info(f"I heard {msg.data}")

    def timer_callback(self):
        msg = String()
        msg.data = f"Hello {self.i}"
        self.pub.publish(msg)
        self.get_logger().info(msg.data)
        self.i += 1


def main():
    rclpy.init()
    node = SubPub()
    rclpy.spin(node)
    rclpy.shutdown()

