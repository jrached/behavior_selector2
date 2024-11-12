cmake_minimum_required(VERSION 3.14.4)
project(behavior_selector)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

find_package(ament_cmake)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rqt_gui REQUIRED)
find_package(rqt_gui_py REQUIRED)

# ROS2:
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/MissionModeChange.srv"
  DEPENDENCIES std_msgs 
)


## Your package locations should be listed before other locations
target_include_directories(${PROJECT_NAME}
  "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
  "$<INSTALL_INTERFACE:include/${PROJECT_NAME}>"
)

install(PROGRAMS scripts/rqt_pkg.py 
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY 
  resource
  DESTINATION share/${PROJECT_NAME}
)

install(FILES 
  plugin.xml
  DESTINATION share/${PROJECT_NAME}
)

ament_package()