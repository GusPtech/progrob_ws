import rclpy
from rclpy.node import Node
from robx7_interfaces.msg import HardwareStatus
from std_srvs.srv import SetBool

class NodoMonitor(Node):
    def __init__(self):
        super().__init__('monitor_node')
        self.declare_parameter('umbral_temperatura', 50)
        self.umbral = self.get_parameter('umbral_temperatura').get_parameter_value().integer_value
        self.get_logger().info(f'Umbral de temperatura configurado a: {self.umbral}')

        self.subscription = self.create_subscription(HardwareStatus, 'hardware_status', self.topic_callback, 10)
        self.srv = self.create_service(SetBool, 'check_system', self.service_callback)
        self.ultimo_estado = None

    def topic_callback(self, msg):
        self.ultimo_estado = msg
        if msg.temperatura > self.umbral:
            self.get_logger().warning(f'¡ADVERTENCIA! Temperatura ({msg.temperatura}) supera el umbral ({self.umbral})')

    def service_callback(self, request, response):
        if self.ultimo_estado is None:
            response.success = False
            response.message = "Sin datos de hardware aún"
        elif self.ultimo_estado.temperatura <= self.umbral and self.ultimo_estado.motores_listos:
            response.success = True
            response.message = "Autorización de movimiento concedida"
        else:
            response.success = False
            response.message = "Bloqueo por estado inseguro o temperatura alta"
        
        self.get_logger().info('Petición de estado recibida y respondida.')
        return response

def main(args=None):
    rclpy.init(args=args)
    nodo = NodoMonitor()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()
