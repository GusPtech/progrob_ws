# Archivo launch para iniciar los 3 nodos del sistema simultaneamente 
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mi_sistema_robot',
            executable='emulador',
            name='emulador_hardware'
        ),
        Node(
            package='mi_sistema_robot',
            executable='monitor',
            name='monitor_node',
            parameters=[
                {'umbral_temperatura': 75}
            ]
        ),
        Node(
            package='mi_sistema_robot',
            executable='operador',
            name='operador_node'
        )
    ])
