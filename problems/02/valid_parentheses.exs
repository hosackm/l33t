defmodule ValidParens do
  def solve(s) do
    recurse(String.graphemes(s), [])
  end

  def recurse([], stack) do
    case stack do
      [] -> true
      _ -> false
    end
  end

  def recurse(s, stack) do
    [ch | rest] = s

    case {ch, stack} do
      {val, _} when val in ["{", "(", "["] ->
        recurse(rest, [ch | stack])

      {"}", ["{" | tail]} ->
        recurse(rest, tail)

      {"]", ["[" | tail]} ->
        recurse(rest, tail)

      {")", ["(" | tail]} ->
        recurse(rest, tail)

      _ ->
        false
    end
  end
end

defmodule ValidParensTest do
  use ExUnit.Case

  test "leetcode examples" do
    assert ValidParens.solve("") == true
    assert ValidParens.solve("[]") == true
    assert ValidParens.solve("[()]") == true
    assert ValidParens.solve("[(})]") == false
    assert ValidParens.solve("([])") == true
  end
end

