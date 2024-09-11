from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter(node: Optional[TreeNode]) -> int:
    """
    Calculates the diameter of the current node.

    Args:
        node Optional[TreeNode]: the node from which to calculate the diameter
    Returns:
        int: the diameter of the node
    """
    _, d = _diameter(node)
    return d


def _diameter(node: Optional[TreeNode]) -> Tuple[int, int]:
    """
    Calculates the diameter of the node. Returns the max
    diameter of all children nodes and the max height of all
    children nodes.

    Args:
        node Optional[TreeNode]: the node from which to calculate height and diameter
    Returns:
        Tuple[int, int]: the max height and max diameter of all children nodes
    """
    if not node:
        return 0, 0

    hl, dl = _diameter(node.left)
    hr, dr = _diameter(node.right)
    return max(hl+1, hr+1), max(dl, dr, hl + hr)


def test_diameter():
    tree = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(4),
            TreeNode(5)
        ),
        TreeNode(3))

    assert diameter(tree) == 3

    tree = TreeNode(1, TreeNode(2), None)
    assert diameter(tree) == 1


if __name__ == "__main__":
    import pytest
    pytest.main(["-xvv", __file__])
