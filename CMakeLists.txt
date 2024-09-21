cmake_minimum_required(VERSION 3.14)

project(l33t-c C)

enable_testing()

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Make interface to glib-2.0
find_package(PkgConfig REQUIRED)
pkg_check_modules(GLIB REQUIRED IMPORTED_TARGET glib-2.0)
add_library(glib INTERFACE)
target_link_libraries(glib INTERFACE PkgConfig::GLIB)

# Make interface for stb
include(FetchContent)
FetchContent_Declare(
    stb
    GIT_REPOSITORY https://github.com/nothings/stb.git
    GIT_TAG        master
)
FetchContent_MakeAvailable(stb)
add_library(stb INTERFACE)
target_include_directories(stb INTERFACE ${stb_SOURCE_DIR})

# Make interface for igraph
FetchContent_Declare(
    igraph
    GIT_REPOSITORY https://github.com/igraph/igraph.git
    GIT_TAG 0.10.13
)
FetchContent_MakeAvailable(igraph)
add_library(libigraph INTERFACE)
target_link_libraries(libigraph INTERFACE igraph)

# Add Criterion library for testing
FetchContent_Declare(
    criterion
    GIT_REPOSITORY https://github.com/Snaipe/Criterion.git
    GIT_TAG        v2.4.1  # Replace with the desired version/tag
)
FetchContent_MakeAvailable(criterion)
set(CRITERION_CMAKE ${criterion_SOURCE_DIR}/dev/cmake/cmake)
set(CMAKE_MODULE_PATH  ${CRITERION_CMAKE} ${CMAKE_MODULE_PATH})
find_package(Criterion REQUIRED)
add_library(criterion INTERFACE)
target_link_libraries(criterion INTERFACE ${CRITERION_LIBRARY})
target_include_directories(criterion INTERFACE ${CRITERION_INCLUDE_DIRS})

# Add strict compiler flags for my code. Won't fix
# upstream dependencies
add_compile_options(-Wall -Wextra -Werror)

# Add existing solutions
add_subdirectory(problems/01)
add_subdirectory(problems/02)
add_subdirectory(problems/03)
add_subdirectory(problems/04)
add_subdirectory(problems/05)
add_subdirectory(problems/06)
add_subdirectory(problems/07)
add_subdirectory(problems/08)
