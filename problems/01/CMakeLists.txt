# stb lib
include(FetchContent)
FetchContent_Declare(
    stb
    GIT_REPOSITORY https://github.com/nothings/stb.git
    GIT_TAG        master
)
FetchContent_MakeAvailable(stb)

# glib library
find_package(PkgConfig REQUIRED)
pkg_check_modules(deps REQUIRED IMPORTED_TARGET glib-2.0)

# add test
add_executable(01_two_sum two_sum.c)
target_link_libraries(01_two_sum PkgConfig::deps)
target_include_directories(01_two_sum PRIVATE ${stb_SOURCE_DIR})
add_test(NAME 01_two_sum COMMAND 01_two_sum)
