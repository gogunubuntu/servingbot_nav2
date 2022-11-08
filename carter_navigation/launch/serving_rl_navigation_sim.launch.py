## Copyright (c) 2021, NVIDIA CORPORATION. All rights reserved.
## NVIDIA CORPORATION and its licensors retain all intellectual property
## and proprietary rights in and to this software, related documentation
## and any modifications thereto.  Any use, reproduction, disclosure or
## distribution of this software and related documentation without an express
## license agreement from NVIDIA CORPORATION is strictly prohibited.

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    use_sim_time = LaunchConfiguration("use_sim_time", default="True")

    map_dir = LaunchConfiguration(
        "map",
        default=os.path.join(
            get_package_share_directory("carter_navigation"), "maps", "carter_warehouse_navigation.yaml"
        ),
    )

    param_dir = LaunchConfiguration(
        "params_file",
        default=os.path.join(
            get_package_share_directory("carter_navigation"), "params", "serving_rl_navigation_params_sim.yaml"
        ),
    )
    nav2_bringup_launch_dir = os.path.join(get_package_share_directory("nav2_bringup"), "launch")
    # four_cam_directly_launch_dir = os.path.join(get_package_share_directory("usb_camera_driver"), "launch")

    rviz_config_dir = os.path.join(get_package_share_directory("carter_navigation"), "rviz2", "carter_navigation.rviz")

    return LaunchDescription(
        [
            DeclareLaunchArgument("map", default_value=map_dir, description="Full path to map file to load"),
            DeclareLaunchArgument(
                "params_file", default_value=param_dir, description="Full path to param file to load"
            ),
            DeclareLaunchArgument(
                "use_sim_time", default_value="true", description="Use simulation (Omniverse Isaac Sim) clock if true"
            ),
            # IncludeLaunchDescription(
            #     PythonLaunchDescriptionSource(os.path.join(nav2_bringup_launch_dir, "rviz_launch.py")),
            #     launch_arguments={"namespace": "", "use_namespace": "False", "rviz_config": rviz_config_dir}.items(),
            # ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([nav2_bringup_launch_dir, "/bringup_launch.py"]),
                launch_arguments={"map": map_dir, "use_sim_time": use_sim_time, "params_file": param_dir}.items(),
            ),
            # IncludeLaunchDescription(
            #     PythonLaunchDescriptionSource([four_cam_directly_launch_dir, "/4cam_directly.launch.py"])
            # ),
        ]
    )
