cmake_minimum_required(VERSION 3.14.4)
project(behavior_selector2)

find_package(ament_cmake)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)
find_package(std_srvs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
    "srv/MissionModeChange.srv"
    DEPENDENCIES std_msgs builtin_interfaces
)

ament_export_dependencies(
    rosidl_default_runtime
    std_msgs
    std_srvs
)

ament_package()