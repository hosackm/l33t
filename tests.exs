ExUnit.start()

test_files = [
  "problems/01/two_sum.exs",
  "problems/02/valid_parentheses.exs",
  "problems/03/merge_two_sorted_lists.exs",
  "problems/04/best_time_to_buy_and_sell_stock.exs"
]

Enum.each(test_files, &Code.require_file/1)
