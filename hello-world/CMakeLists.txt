cmake_minimum_required(VERSION 3.27)
project(helloworld C)

find_package(ZLIB REQUIRED)

add_executable(${PROJECT_NAME} src/main.c)

target_link_libraries(${PROJECT_NAME} ZLIB::ZLIB)
