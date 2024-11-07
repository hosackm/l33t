defmodule TwoSum do
  def iterative(nums, target) do
    nums
    |> Enum.with_index()
    |> Enum.reduce_while(%{}, fn {num, idx}, acc ->
      complement = Map.get(acc, target - num)

      if complement do
        {:halt, [complement, idx]}
      else
        {:cont, Map.put(acc, num, idx)}
      end
    end)
  end

  def recursive(nums, target, cache \\ %{}, index \\ 0) do
    [num | rest] = nums
    comp = target - num

    case Map.get(cache, comp) do
      nil -> recursive(rest, target, Map.put(cache, num, index), index + 1)
      comp_index -> [comp_index, index]
    end
  end
end

defmodule TwoSumTest do
  use ExUnit.Case

  test "leetcode examples" do
    assert TwoSum.iterative([2, 7, 11, 15], 9) == [0, 1]
    assert TwoSum.recursive([2, 7, 11, 15], 9) == [0, 1]
    assert TwoSum.iterative([3, 2, 4], 6) == [1, 2]
    assert TwoSum.recursive([3, 2, 4], 6) == [1, 2]
    assert TwoSum.iterative([3, 3], 6) == [0, 1]
    assert TwoSum.recursive([3, 3], 6) == [0, 1]
  end
end
