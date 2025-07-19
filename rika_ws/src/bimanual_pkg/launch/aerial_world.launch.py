from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.actions import SetEnvironmentVariable
def generate_launch_description():
    return LaunchDescription([
        #SetEnvironmentVariable(name='GAZEBO_GUI_PLUGIN', value=''),
        #SetEnvironmentVariable(name='GAZEBO_PLUGIN_PATH', value=''),
        #SetEnvironmentVariable('LIBGL_ALWAYS_SOFTWARE', '1'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('gazebo_ros'),
                    'launch',
                    'gazebo.launch.py'
                ])
            ]),
            launch_arguments={
                'world': PathJoinSubstitution([
                    FindPackageShare('bimanual_pkg'),
                    'worlds',
                    'aerial_world.world'
                ])
            }.items()
        ),
    ])
