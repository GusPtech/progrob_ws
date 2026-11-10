from setuptools import find_packages, setup

package_name = 'mi_sistema_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[('share/' + package_name + '/launch', ['launch/hardware_system.launch.py']),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='GusPtech',
    maintainer_email='gustavo.gonzalez1762@alumnos.ugd.mx',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': ['emulador = mi_sistema_robot.emulador:main',
    'monitor = mi_sistema_robot.monitor:main',
    'operador = mi_sistema_robot.operador:main',
        ],
    },
)
