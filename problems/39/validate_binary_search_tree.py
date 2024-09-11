from dataclasses import dataclass
from typing import Tuple


INTMIN = -(2**32)
INTMAX = 2**32


# @dataclass
# class ValidSubtreeResult:
#     is_valid: bool = True
#     left_max: int = INTMIN
#     right_min: int = INTMAX


# is subtree valid,
ValidSubtreeResult = Tuple[bool, int, int]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid(root: TreeNode | None) -> bool:
    valid, _, _ = is_valid_subtree(root)
    return valid


def is_valid_subtree(node):
    if not node:
        return True, INTMIN, INTMAX

    left_valid, left_max, left_min = is_valid_subtree(node.left)
    right_valid, right_max, right_min = is_valid_subtree(node.right)

    # invalid subtree
    if (
        not left_valid
        or not right_valid
        or left_max >= node.val
        or right_min <= node.val
    ):
        return False, left_max, right_min

    return True, max(node.val, left_max, right_max), min(node.val, right_min, left_min)


def test_is_valid():
    tree = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid(tree) == True
    tree = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid(tree) == False
    tree = TreeNode(2, TreeNode(2), TreeNode(2))
    assert is_valid(tree) == False


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
