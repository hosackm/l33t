ExUnit.start()

test_files = [
  "problems/01/two_sum.exs"
]

Enum.each(test_files, &Code.require_file/1)
