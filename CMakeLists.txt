cmake_minimum_required(VERSION 3.16)

project(l33t-c C)

enable_testing()

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_compile_options(-Wall -Wextra -Werror)

add_subdirectory(problems/01)
add_subdirectory(problems/02)
add_subdirectory(problems/03)
add_subdirectory(problems/07)
