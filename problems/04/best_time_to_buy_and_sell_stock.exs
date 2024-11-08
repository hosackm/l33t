defmodule BuySellStock do
  def solve(nums) do
    max_profit(nums, 0, nil)
  end

  defp max_profit([], max_profit, _min_price), do: max_profit

  defp max_profit([price | rest], max_profit, nil) do
    max_profit(rest, max_profit, price)
  end

  defp max_profit([price | rest], max_profit, min_price) do
    profit = price - min_price
    max_profit = max(max_profit, profit)
    min_price = min(min_price, price)
    max_profit(rest, max_profit, min_price)
  end
end

defmodule Tests do
  use ExUnit.Case

  test "something" do
    assert BuySellStock.solve([7, 1, 5, 3, 6, 4]) == 5
    assert BuySellStock.solve([7, 6, 4, 3, 1]) == 0
    assert BuySellStock.solve([]) == 0
  end
end
