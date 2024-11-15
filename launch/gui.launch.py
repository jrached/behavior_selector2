import os 
from launch import LaunchDescription
from launch_ros.actions import Node 
from launch.actions import DeclareLaunchArgument, GroupAction 
from launch.substitutions import LaunchConfiguration, EnvironmentVariable
from launch.actions import IncludeLaunchDescription 
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory 

def generate_launch_description():

    rqt_node = Node(
        package="rqt_gui",
        executable="rqt_gui",
        name="rqt_gui",
        arguments=["--perspective-file",
        os.path.join(get_package_share_directory('behavior_selector2'),
                    'cfg', 'default.perspective')]
    )

    behavior_node = Node(
        package="behavior_selector2",
        executable="behavior_selector_node",
        name="behavior_selector",
        output="screen"
    )


    return LaunchDescription([
        rqt_node,
        behavior_node
    ])