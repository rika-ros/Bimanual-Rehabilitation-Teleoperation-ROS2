#!/usr/bin/env python3

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    
    # Package Directories
    pkg_gazebo_ros = FindPackageShare(package='gazebo_ros').find('gazebo_ros')   
    pkg_share = FindPackageShare(package='bimanual_pkg').find('bimanual_pkg')  # Replace with your actual package name
    
    # Path to the world file
    world_file_name = 'aerial_world.world'
    world_path = os.path.join(pkg_share, 'worlds', world_file_name)
    
    # Path to the URDF file
    urdf_file_name = 'box_with_side_box_4P.urdf'  # Replace with your actual URDF filename
    urdf_path = os.path.join(pkg_share, 'urdf', urdf_file_name)
    
    # Launch configuration variables
    use_sim_time = LaunchConfiguration('use_sim_time')
    x_pose = LaunchConfiguration('x_pose')
    y_pose = LaunchConfiguration('y_pose')
    z_pose = LaunchConfiguration('z_pose')
    
    # Declare the launch arguments
    declare_use_sim_time_cmd = DeclareLaunchArgument(
        name='use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true')
    
    declare_x_position_cmd = DeclareLaunchArgument(
        name='x_pose',
        default_value='0.0',
        description='Initial x position of the robot')
        
    declare_y_position_cmd = DeclareLaunchArgument(
        name='y_pose',
        default_value='0.0',
        description='Initial y position of the robot')
        
    declare_z_position_cmd = DeclareLaunchArgument(
        name='z_pose',
        default_value='0.5',
        description='Initial z position of the robot')
    
    # Start Gazebo server
    start_gazebo_server_cmd = ExecuteProcess(
        cmd=['gzserver', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', world_path],
        cwd=[pkg_share], output='screen')

    # Start Gazebo client    
    start_gazebo_client_cmd = ExecuteProcess(
        cmd=['gzclient'],
        cwd=[pkg_share], output='screen')

    # Robot State Publisher
    robot_state_publisher_cmd = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'use_sim_time': use_sim_time,
            'robot_description': open(urdf_path, 'r').read()
        }]
    )

    # Spawn the robot in Gazebo
    spawn_entity_cmd = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'floating_box',
            '-topic', 'robot_description',
            '-x', x_pose,
            '-y', y_pose,
            '-z', z_pose
        ],
        output='screen'
    )

    # Joint State Publisher (if needed for visualization)
    joint_state_publisher_cmd = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    # Create the launch description and populate
    ld = LaunchDescription()

    # Declare the launch options
    ld.add_action(declare_use_sim_time_cmd)
    ld.add_action(declare_x_position_cmd)
    ld.add_action(declare_y_position_cmd)
    ld.add_action(declare_z_position_cmd)

    # Add the actions to launch all of the navigation nodes
    ld.add_action(start_gazebo_server_cmd)
    ld.add_action(start_gazebo_client_cmd)
    ld.add_action(robot_state_publisher_cmd)
    ld.add_action(spawn_entity_cmd)
    ld.add_action(joint_state_publisher_cmd)

    return ld