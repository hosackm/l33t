add_executable(07_valid_anagram)

find_package(PkgConfig REQUIRED)
pkg_check_modules(deps REQUIRED IMPORTED_TARGET glib-2.0)
target_link_libraries(07_valid_anagram PkgConfig::deps)
target_sources(07_valid_anagram PRIVATE valid_anagram.c)

add_test(NAME 07_valid_anagram COMMAND 07_valid_anagram)
