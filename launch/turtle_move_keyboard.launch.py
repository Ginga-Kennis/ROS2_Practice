import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim_node',
        ),
        Node(
            prefix="xterm -e",
            package='turtlesim_test',
            executable='teleop_keyboard',
            name='teleop_keyboard',
            remappings=[("/cmd_vel","/turtle1/cmd_vel")],
        ),
        
        
    ])

