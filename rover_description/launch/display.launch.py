import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node

def generate_launch_description():
    pkg_path = get_package_share_directory('rover_description')
    xacro_file = os.path.join(pkg_path,'urdf','rover.urdf.xacro')

    robot_description = Command(['xacro ',xacro_file])

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description':robot_description}]
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    )
    rviz_Node=Node(
        package='rviz2',
        executable='rviz2'
    )
    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_Node
    ])