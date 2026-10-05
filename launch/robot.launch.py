import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():

    package_dir = get_package_share_directory('four_wheel_robot')

    urdf_file = os.path.join(
        package_dir,
        'urdf',
        'my_robot.urdf'
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={
            'gz_args': '-r empty.sdf'
        }.items()
    )

    robot_description = open(urdf_file).read()

    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-string',
            robot_description,
            '-name',
            'four_wheel_robot',
            '-allow_renaming',
            'true'
             '-z',
            '0.2'

        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn_robot
    ])
