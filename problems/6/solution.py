from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert(tree: Optional[TreeNode] = None) -> Optional[TreeNode]:
    """
    Invert a binary tree by swapping the children of each node.

    Args:
        tree (TreeNode): tree to invert. Can be None.
    Returns:
        TreeNode: the inverse of the tree. If the tree was None, then None is returned
    """
    if tree is None:
        return None

    invert(tree.left)
    invert(tree.right)
    tree.left, tree.right = tree.right, tree.left

    return tree


def test_invert_binary_tree():
    # case 1
    first = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(
            7,
            TreeNode(6),
            TreeNode(9)
        )
    )
    invert(first)
    output = [
        first.val,
        first.left.val, first.right.val,
        first.left.left.val, first.left.right.val,
        first.right.left.val, first.right.right.val,
    ]
    expected = [4, 7, 2, 9, 6, 3, 1]
    assert output == expected

    # case 2
    second = TreeNode(2, TreeNode(1), TreeNode(3))
    invert(second)
    assert [2, 3, 1] == [second.val, second.left.val, second.right.val]

    # case 3
    assert invert() is None


if __name__ == "__main__":
    import pytest
    pytest.main(["-xv", __file__])
