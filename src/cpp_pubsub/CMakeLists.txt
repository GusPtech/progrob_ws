cmake_minimum_required(VERSION 3.8)
project(cpp_pubsub)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Librerías que necesita el paquete
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# Programa publisher_cpp
add_executable(publisher_cpp src/publisher_cpp.cpp)
target_link_libraries(publisher_cpp PUBLIC rclcpp::rclcpp ${std_msgs_TARGETS})

# Programa subscriber_cpp
add_executable(subscriber_cpp src/subscriber_cpp.cpp)
target_link_libraries(subscriber_cpp PUBLIC rclcpp::rclcpp ${std_msgs_TARGETS})

# Instalar los programas para poder usar "ros2 run"
install(TARGETS publisher_cpp subscriber_cpp DESTINATION lib/${PROJECT_NAME})

ament_package()
