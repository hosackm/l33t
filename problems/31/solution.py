class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    """
    Returns a list of tree nodes grouped into lists by
    level number in order.

    For example:
          3
    9          20
           15      7
    will return [[3], [9, 20], [15, 7]]
    """
    if root is None:
        return []

    answer = []
    level = 0
    current_level = []
    for node in bfs_nodes(root):
        lvl, n = node
        if lvl > level:
            if current_level:
                answer.append(current_level)

            current_level = []
            level = lvl

        current_level.append(n)

    if current_level:
        answer.append(current_level)

    return answer


def bfs_nodes(root):
    nodes = []
    queue = [(0, root)]
    while queue:
        lvl, node = queue.pop(0)
        nodes.append((lvl, node.val))

        if node.left:
            queue.append((lvl + 1, node.left))
        if node.right:
            queue.append((lvl + 1, node.right))

    return nodes


def level_order_2(root):
    if root is None:
        return []

    level = 0
    queue = [(0, root)]
    answer = []

    current = []
    while queue:
        lvl, node = queue.pop(0)
        if lvl != level:
            if current:
                answer.append(current)
            level = lvl
            current = []
        current.append(node.val)

        if node.left:
            queue.append((lvl + 1, node.left))
        if node.right:
            queue.append((lvl + 1, node.right))

    if current:
        answer.append(current)

    return answer


def test_level_order():
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order_2(tree) == [[3], [9, 20], [15, 7]]


#    assert level_order(None) == []
#    assert level_order(TreeNode(1)) == [[1]]


def test_bfs_nodes():
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert bfs_nodes(tree) == [(0, 3), (1, 9), (1, 20), (2, 15), (2, 7)]


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
