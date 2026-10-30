from setuptools import find_packages, setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vboxuser',
    maintainer_email='vboxuser@todo.todo',
    description='Publisher y Subscriber en Python para la Actividad 2',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'publisher_py = py_pubsub.publisher_py:main',
            'subscriber_py = py_pubsub.subscriber_py:main',
        ],
    },
)
