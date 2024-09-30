# Create library for shared data structure code between solutions
add_library(l33t STATIC
    src/tree.c
    src/list.c
    src/stack.c
)
target_include_directories(l33t PUBLIC include)
target_link_libraries(l33t PRIVATE stb)

# Add lib test executable
add_executable(test_l33t_lib
    test/test_list.c
    test/test_tree.c
    test/test_stack.c
)
target_link_libraries(test_l33t_lib PRIVATE l33t criterion)

add_test(NAME test_l33t_lib COMMAND test_l33t_lib)
