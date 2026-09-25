import rclpy
from rclpy.node import Node


class MojNode(Node):
    def __init__(self):
        super().__init__('moj_node')
        self.get_logger().info('Zdravo, ja sam moj_node!')
        

def main():
    rclpy.init()
    node = MojNode()
    rclpy.spin(node)