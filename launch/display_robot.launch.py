from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(
                '/home/manjushree/ros2_ws/src/my_robot_description/urdf/my_robot.urdf.xacro'
            ).read()}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', '/home/manjushree/ros2_ws/src/my_robot_description/rviz/robot_model.rviz']
        )
    ])
