import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SubscriberPy(Node):
    """Nodo que escucha el topic 'chatter' y muestra cada mensaje recibido."""

    def __init__(self):
        super().__init__('subscriber_py')
        # Suscripción: tipo String, topic 'chatter', cola de 10 mensajes.
        # Cada mensaje que llega ejecuta listener_callback.
        self.subscription = self.create_subscription(
            String, 'chatter', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info(f"Python recibió: '{msg.data}'")


def main(args=None):
    rclpy.init(args=args)
    node = SubscriberPy()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
