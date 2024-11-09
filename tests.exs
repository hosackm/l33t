ExUnit.start()

test_files = [
  "problems/01/two_sum.exs",
  "problems/02/valid_parentheses.exs",
  "problems/03/merge_two_sorted_lists.exs",
  "problems/04/best_time_to_buy_and_sell_stock.exs",
  "problems/05/valid_palindrome.exs",
  "problems/06/invert_binary_tree.exs"
]

Enum.each(test_files, &Code.require_file/1)
