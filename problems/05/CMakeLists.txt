add_executable(05_valid_palindrome)
target_sources(05_valid_palindrome PRIVATE valid_palindrome.c)
target_link_libraries(05_valid_palindrome PRIVATE criterion)
add_test(NAME 05_valid_palindrome COMMAND 05_valid_palindrome --color=always)
