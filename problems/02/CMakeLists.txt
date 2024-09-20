add_executable(02_valid_parentheses)

find_package(PkgConfig REQUIRED)
pkg_check_modules(deps REQUIRED IMPORTED_TARGET glib-2.0)
target_link_libraries(02_valid_parentheses PkgConfig::deps)
target_sources(02_valid_parentheses PRIVATE valid_parentheses.c)

# stb lib
include(FetchContent)
FetchContent_Declare(
    stb
    GIT_REPOSITORY https://github.com/nothings/stb.git
    GIT_TAG        master
)
FetchContent_MakeAvailable(stb)
target_include_directories(02_valid_parentheses PRIVATE ${stb_SOURCE_DIR})

add_test(NAME 02_valid_parentheses COMMAND 02_valid_parentheses)
