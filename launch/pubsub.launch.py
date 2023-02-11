import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim_test',
            executable='publisher',
            name='publisher',
        ),
        Node(
            prefix="xterm -e",
            package='turtlesim_test',
            executable='sub_pub',
            name='subpub',
        ),
        Node(
            prefix="xterm -e",
            package='turtlesim_test',
            executable='subscriber',
            name='subscriber',
            remappings=[('/Message','/Topic')]
        ),
    ])

