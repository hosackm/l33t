add_executable(07_valid_anagram)
target_link_libraries(07_valid_anagram PRIVATE criterion)
target_sources(07_valid_anagram PRIVATE valid_anagram.c)
add_test(NAME 07_valid_anagram COMMAND 07_valid_anagram)
