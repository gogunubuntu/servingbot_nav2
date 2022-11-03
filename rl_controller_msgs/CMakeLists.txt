cmake_minimum_required(VERSION 3.5)
project(rl_controller_msgs)

find_package(builtin_interfaces REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(rl_controller_msgs
    "srv/CalcRlVel.srv"
    DEPENDENCIES std_msgs builtin_interfaces
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()
