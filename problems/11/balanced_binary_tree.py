from typing import Optional, Tuple
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(tree: Optional[TreeNode]) -> Tuple[bool, int]:
    if not tree:
        return True, 0

    lb, lhs = is_balanced(tree.left)
    rb, rhs = is_balanced(tree.right)

    balanced = lb and rb and abs(lhs - rhs) <= 1
    height = max(lhs, rhs) + 1
    return balanced, height


def get_tree(vals):
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    length = len(nodes)
    for i, n in enumerate(nodes):
        left = (2 * i) + 1
        right = (2 * i) + 2
        if left < length and nodes[left]:
            n.left = nodes[left]
        if right < length and nodes[left]:
            n.right = nodes[right]

    return nodes[0]


def test_is_balanced():
    tree = get_tree([3, 9, 20, None, None, 15, 7])
    assert is_balanced(tree) == (True, 3)
    tree = get_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    assert is_balanced(tree) == (False, 4)
    tree = get_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
    assert is_balanced(tree) == (False, 4)


def test_get_tree():
    tree = get_tree([3, 9, 20, None, None, 15, 7])
    assert tree.val == 3
    assert tree.left.val == 9
    assert tree.right.val == 20
    assert tree.right.left.val == 15
    assert tree.right.right.val == 7

    tree = get_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    assert tree.val == 1
    assert tree.left.val == 2
    assert tree.left.val == 2
    assert tree.left.left.left.val == 4
    assert tree.left.left.right.val == 4
    assert tree.right.val == 2



if __name__ == "__main__":
    import pytest
    pytest.main(["-xvvs", __file__])
