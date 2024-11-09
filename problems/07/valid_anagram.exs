defmodule ValidAnagram do
  def solve(first, second) do
    count(first) == count(second)
  end

  def count(s) do
    count(String.to_charlist(s), %{})
  end

  def count([], acc), do: acc

  def count([ch | rest], acc) do
    case Map.fetch(acc, ch) do
      {:ok, cnt} -> count(rest, Map.put(acc, ch, cnt + 1))
      :error -> count(rest, Map.put(acc, ch, 1))
    end
  end
end

defmodule ValidAnagramTest do
  use ExUnit.Case

  test "leetcode tests" do
    assert ValidAnagram.solve("anagram", "nagaram") == true
    assert ValidAnagram.solve("rat", "car") == false
  end
end
