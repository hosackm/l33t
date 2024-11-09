defmodule TreeNode do
  @type t :: %__MODULE__{
          val: integer,
          left: TreeNode.t() | nil,
          right: TreeNode.t() | nil
        }
  defstruct val: 0, left: nil, right: nil

  def invert_tree(nil), do: nil

  def invert_tree(tree) do
    %TreeNode{
      val: tree.val,
      left: invert_tree(tree.right),
      right: invert_tree(tree.left)
    }
  end
end

defmodule TestTreeInvert do
  use ExUnit.Case

  test "leetcode 1" do
    tree = %{
      val: 4,
      left: %{
        val: 2,
        left: %{val: 1, left: nil, right: nil},
        right: %{val: 3, left: nil, right: nil}
      },
      right: %{
        val: 7,
        left: %{val: 6, left: nil, right: nil},
        right: %{val: 9, left: nil, right: nil}
      }
    }

    inverted = TreeNode.invert_tree(tree)
    assert inverted.val == 4
    assert inverted.left.val == 7
    assert inverted.left.left.val == 9
    assert inverted.left.right.val == 6
    assert inverted.right.val == 2
    assert inverted.right.left.val == 3
    assert inverted.right.right.val == 1
  end

  test "leetcode 2" do
    tree = %{
      val: 2,
      left: %{
        val: 1,
        left: nil,
        right: nil
      },
      right: %{
        val: 3,
        left: nil,
        right: nil
      }
    }

    inverted = TreeNode.invert_tree(tree)
    assert inverted.val == 2
    assert inverted.left.val == 3
    assert inverted.right.val == 1
    assert inverted.left.left == nil
    assert inverted.left.right == nil
    assert inverted.right.left == nil
    assert inverted.right.right == nil
  end

  test "leetcode 3" do
    assert TreeNode.invert_tree(nil) == nil
  end
end
