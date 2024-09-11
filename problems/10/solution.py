class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def from_list(cls, nodes):
        nodes = [TreeNode(n) for n in nodes]
        for i, node in enumerate(nodes):
            left = (2 * i) + 1
            if left < len(nodes):
                node.left = nodes[left]

            right = (2 * i) + 2
            if right < len(nodes):
                node.right = nodes[right]
        return nodes[0]


    def to_list(self):
        nodes = []
        queue = [self]
        while queue:
            current = queue.pop(0)
            nodes.append(current.val if current else None)
            if current and current.left:
                queue.append(current.left)
            if current and current.right:
                queue.append(current.right)
        return nodes


def find_lca(root: TreeNode, p: TreeNode, q: TreeNode):
    """
    Returns the least common ancestor shared between p and q.
    """
    cur = root
    while cur:
        if p < cur.val and q < cur.val:
            cur = root.left
            continue
        elif p > cur.val and q > cur.val:
            cur = root.right
            continue
        return cur.val


def bfs(root):
    visited = {}  # 3.7+ dict maintains insertion order
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.val is None:
            continue

        if current not in visited:
            visited[current.val] = True
            if current.left and current.left.val not in visited:
                queue.append(current.left)
            if current.right and current.right.val not in visited:
                queue.append(current.right)

    return list(visited.keys())


def dfs(root):
    visited = {}  # 3.7+ dict maintains insertion order
    stack = [root]
    while stack:
        current = stack.pop()
        if current.val is None:
            continue

        if current not in visited:
            visited[current.val] = True
            if current.right and current.right.val not in visited:
                stack.append(current.right)
            if current.left and current.left.val not in visited:
                stack.append(current.left)

    return list(visited.keys())


def test_lca():
    nodes = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    tree = TreeNode.from_list(nodes)
    assert find_lca(tree, 2, 8) == 6
    assert find_lca(tree, 2, 4) == 2
    tree = TreeNode.from_list([2, 1])
    assert find_lca(tree, 2, 1) == 2


def test_bfs():
    tree = TreeNode.from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert bfs(tree) == [6, 2, 8, 0, 4, 7, 9, 3, 5]


def test_dfs():
    tree = TreeNode.from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert dfs(tree) == [6, 2, 0, 4, 3, 5, 8, 7, 9]


if __name__ == "__main__":
    import pytest
    pytest.main(["-xvvs", __file__])
