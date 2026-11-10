import rclpy
from rclpy.node import Node
from robx7_interfaces.msg import HardwareStatus
import random

class EmuladorHardware(Node):
    def __init__(self):
        super().__init__('emulador_hardware')
        self.publisher_ = self.create_publisher(HardwareStatus, 'hardware_status', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.temperatura_actual = 40

    def timer_callback(self):
        msg = HardwareStatus()
        self.temperatura_actual += random.randint(-2, 5)
        msg.temperatura = self.temperatura_actual
        msg.motores_listos = self.temperatura_actual < 80
        msg.debug_msg = "Operación normal" if msg.motores_listos else "Fallo: Sobrecalentamiento"
        
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: Temp={msg.temperatura}, Motores={msg.motores_listos}')

def main(args=None):
    rclpy.init(args=args)
    nodo = EmuladorHardware()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()
