add_executable(03_merge_sorted_lists)
target_sources(03_merge_sorted_lists PRIVATE merge_two_sorted_lists.c)
target_link_libraries(03_merge_sorted_lists PRIVATE glib)
add_test(NAME 03_merge_sorted_lists COMMAND 03_merge_sorted_lists)

add_custom_target(leaks
    COMMAND leaks --atExit -- "${CMAKE_CURRENT_BINARY_DIR}/03_merge_sorted_lists"
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    DEPENDS 03_merge_sorted_lists
    COMMENT "Running leaks on executable"
    VERBATIM
)
