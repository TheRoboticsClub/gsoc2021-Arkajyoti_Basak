cmake_minimum_required(VERSION 3.0.2)
project(assets)

find_package(catkin REQUIRED COMPONENTS)

catkin_package()

install(DIRECTORY
  models
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
