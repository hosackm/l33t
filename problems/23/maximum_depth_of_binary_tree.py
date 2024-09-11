from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def test_max_depth():
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(tree) == 3

    tree = TreeNode(1, None, TreeNode(2))
    assert max_depth(tree) == 2


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
