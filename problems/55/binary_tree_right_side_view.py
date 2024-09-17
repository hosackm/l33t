from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side(root: TreeNode | None) -> TreeNode | None:
    """
    Return a list of the rightmost element in each row of a tree.
    """
    if not root:
        return []

    return [row[-1].val for row in tree_rows(root)]


def tree_rows(root: TreeNode | None) -> list[list[TreeNode]]:
    """
    Return a list containing a list of nodes in each level of a tree.
    """
    queue = [(root, 0)]
    rows = defaultdict(list)

    while queue:
        node, level = queue.pop(0)
        rows[level].append(node)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return [rows[i] for i in range(len(rows))]


def test_right_side():
    TN = TreeNode
    tree = TN(1, TN(2, None, TN(5)), TN(3, None, TN(4)))
    assert right_side(tree) == [1, 3, 4]

    tree = TN(1, None, TN(3))
    assert right_side(tree) == [1, 3]

    tree = None
    assert right_side(tree) == []


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
