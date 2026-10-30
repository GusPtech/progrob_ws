import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PublisherPy(Node):
    """Nodo que publica un mensaje de texto cada 500 ms en el topic 'chatter'."""

    def __init__(self):
        super().__init__('publisher_py')
        # Crea el publisher: tipo String, topic 'chatter', cola de 10 mensajes
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        # Temporizador que llama a timer_callback cada 0.5 segundos
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hola desde Python #{self.count}'
        self.count += 1
        self.get_logger().info(f"Publicando: '{msg.data}'")
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PublisherPy()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
