class TreeNode:
    def __init__(self, x: int, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def lca(tree: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    path_p, path_q = find_path(tree, p, q)

    i = 0
    shortest = min(len(path_p), len(path_q))
    while i < shortest - 1 and path_p[i + 1] == path_q[i + 1]:
        i += 1

    return path_p[i]


def lca_recursive(tree, p, q):
    if tree is None:
        return None
    if tree.val == p.val:
        return p
    if tree.val == q.val:
        return q

    left = lca_recursive(tree.left, p, q)
    right = lca_recursive(tree.right, p, q)
    if left and not right:
        return left
    if right and not left:
        return right
    if left and right:
        return tree
    return None


def find_path(tree: TreeNode, tgt1: TreeNode, tgt2: TreeNode):
    """
    Iterative breadth first search through children nodes. When
    tgt is found, the path to tgt is returned.

    If tgt is not in the tree and empty list is returned.
    """
    queue = [(tree, [])]
    first = None
    second = None
    while queue:
        # node, path = queue.pop(-1)
        node, path = queue.pop()

        if node.val == tgt1.val:
            first = path + [node]
        if node.val == tgt2.val:
            second = path + [node]
        if first and second:
            return [first, second]

        if node.left:
            queue.append((node.left, path + [node]))

        if node.right:
            queue.append((node.right, path + [node]))

    return []


def test_lca_non_bst():
    p = TreeNode(
        5,
        TreeNode(6),
        TreeNode(2, TreeNode(7), TreeNode(4)),
    )
    q = TreeNode(1, TreeNode(0), TreeNode(8))
    tree = TreeNode(
        3,
        p,
        q,
    )
    # assert lca(tree, p, q) == tree
    assert lca_recursive(tree, p, q) == tree

    nodes = [
        TreeNode(n) if n is not None else None
        for n in (3, 5, 1, 6, 2, 0, 8, None, None, 7, 4)
    ]
    for i in range((len(nodes) - 1) // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        nodes[i].left = nodes[left]
        nodes[i].right = nodes[right]
    tree = nodes[0]

    # ancestor = lca(tree, nodes[1], nodes[-1])
    ancestor = lca_recursive(tree, nodes[1], nodes[-1])
    assert ancestor.val == nodes[1].val


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
