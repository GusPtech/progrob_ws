import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class NodoOperador(Node):
    def __init__(self):
        super().__init__('operador_node')
        self.cli = self.create_client(SetBool, 'check_system')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servicio no disponible, esperando...')
        
        self.timer = self.create_timer(3.0, self.hacer_peticion)

    def hacer_peticion(self):
        req = SetBool.Request()
        req.data = True
        future = self.cli.call_async(req)
        future.add_done_callback(self.callback_respuesta)

    def callback_respuesta(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Respuesta del servidor: {response.message}')
        except Exception as e:
            self.get_logger().error(f'Fallo al llamar al servicio: {e}')

def main(args=None):
    rclpy.init(args=args)
    nodo = NodoOperador()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

