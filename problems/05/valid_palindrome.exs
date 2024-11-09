defmodule ValidPalindrome do
  require Integer

  def valid?(s) do
    valid_palindrome(s)
  end

  defp valid_palindrome(s) do
    mid = Integer.floor_div(String.length(s), 2)

    front =
      String.to_charlist(s)
      |> Enum.take(mid)

    back =
      String.to_charlist(s)
      |> Enum.reverse()
      |> Enum.take(mid)

    front == back
  end
end

defmodule TestValidPalindrome do
  use ExUnit.Case

  test "leetcode examples" do
    assert ValidPalindrome.valid?("racecar") == true
    assert ValidPalindrome.valid?("raceacar") == false
    assert ValidPalindrome.valid?(" ") == true
  end
end
