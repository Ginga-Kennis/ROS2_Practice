import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber(Node):
    def __init__(self):
        super().__init__("subscriber")
        self.sub = self.create_subscription(String,'Message',self.callback,10)
    
    def callback(self,msg):
        self.get_logger().info(f"I heard {msg.data}")

def main():
    rclpy.init()
    node = Subscriber()
    rclpy.spin(node)
    rclpy.shutdown()


