defmodule MergeTwoSortedLists do
  def solve(left, right) do
    merge([], left, right)
    |> Enum.reverse()
  end

  def merge(acc, [], []), do: acc
  def merge(acc, [], right), do: right ++ acc
  def merge(acc, left, []), do: left ++ acc

  def merge(acc, left, right) do
    case {left, right} do
      {[lh | lt], [rh | _]} when lh < rh -> merge([lh | acc], lt, right)
      {left, [rh | rt]} -> merge([rh | acc], rt, left)
    end

    # also works, a bit cleaner but more verbose
    # case {left, right} do
    #   {[lh | lt], [rh | rt]} ->
    #     if lh < rh do
    #       merge([lh | acc], lt, right)
    #     else
    #       merge([rh | acc], rt, left)
    #     end
    # end
  end
end

defmodule MergeTwoSortedListsTests do
  use ExUnit.Case

  test "something" do
    assert MergeTwoSortedLists.solve([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]
    assert MergeTwoSortedLists.solve([], []) == []
    assert MergeTwoSortedLists.solve([], [0]) == [0]
  end
end
