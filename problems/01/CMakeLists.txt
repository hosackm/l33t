add_executable(01_two_sum two_sum.c)
target_link_libraries(01_two_sum PRIVATE criterion)
target_link_libraries(01_two_sum PRIVATE stb)
add_test(NAME 01_two_sum COMMAND 01_two_sum)
