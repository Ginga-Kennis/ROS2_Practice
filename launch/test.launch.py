import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='turtle1',
            executable='turtlesim_node',
            name='kame',
            remappings=[("/turtle1/turtle1/cmd_vel","/turtle1/cmd_vel")],
        ),
        Node(
            package='turtlesim',
            namespace='turtle2',
            executable='turtlesim_node',
            name='kame',
            remappings=[("/turtle2/turtle1/cmd_vel","/turtle2/cmd_vel")],
        ),
        Node(
            prefix="xterm -e",
            namespace="turtle1",
            package="turtlesim",
            executable="turtle_teleop_key",
            remappings=[("/turtle1/turtle1/cmd_vel","/turtle1/cmd_vel")],
        ),
        Node(
            prefix="xterm -e",
            namespace="turtle2",
            package="turtlesim",
            executable="turtle_teleop_key",
            remappings=[("/turtle2/turtle1/cmd_vel","/turtle2/cmd_vel")],
        ),
        
    ])

