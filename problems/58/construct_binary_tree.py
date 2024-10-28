class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_optimized(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """
    Use dictionary to quickly segment preorder and inorder lists
    into left and right subtrees.

    Args:
        pre (list[int]): the preorder traversal ordering
        ino (list[int]): the inorder traversal ordering
    Returns:
        TreeNode | None: the tree constructed using both traversals
    """

    def recurse(pstart, pend, istart, iend, index) -> TreeNode | None:
        """
        Recursively build the tree from preorder and inorder lists by
        slicing the two lists from pre[pstart:pend] and ino[istart:iend].
        Uses an index to lookup the index of pre[0] in ino to find the
        midway point the segments left and right subtrees.
        """
        if pend <= pstart:
            return None
        if pend - pstart == 1:
            return TreeNode(preorder[pstart])

        root = preorder[pstart]
        mid = index[root]
        t = TreeNode(root)

        # recurse down left and right subtrees
        left = pstart + 1
        preorder_middle = left + mid - istart

        t.left = recurse(left, preorder_middle, istart, mid, index)
        t.right = recurse(preorder_middle, pend, mid + 1, iend, index)

        return t

    index = {num: i for i, num in enumerate(inorder)}
    return recurse(0, len(preorder), 0, len(inorder), index)


def construct(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Constructs a binary tree given its preoder and inorder traversal.
    This is not the optimal solution because the index method is used
    to find the midpoint of the inorder list. See construct_optimized
    for a better solution.

    Args:
        preorder (list[int]): the preorder traversal ordering
        inorder (list[int]): the inorder traversal ordering
    Returns:
        TreeNode | None: the tree constructed using both traversals
    """
    if not preorder:
        return None
    if len(preorder) == 1:
        return TreeNode(preorder[0])

    root = preorder[0]
    mid = inorder.index(root)

    # slice out the left and right subtrees
    pleft = preorder[1 : mid + 1]
    pright = preorder[mid + 1 :]
    ileft = inorder[:mid]
    iright = inorder[mid + 1 :]

    t = TreeNode(root)
    t.left = construct(pleft, ileft)
    t.right = construct(pright, iright)

    return t


def test_construct():
    # Happy Case. Each height level is full.
    #       1
    #    2    3
    #  4  5  6  7
    p = [1, 2, 4, 5, 3, 6, 7]
    i = [4, 2, 5, 1, 6, 3, 7]
    t = construct_optimized(p, i)
    assert t.val == 1
    assert t.left.val == 2
    assert t.left.left.val == 4
    assert t.left.right.val == 5
    assert t.right.val == 3
    assert t.right.left.val == 6
    assert t.right.right.val == 7

    # More difficult. Missing nodes mean the indexes don't line up.
    #       3
    #    9    20
    #       15  7
    p = [3, 9, 20, 15, 7]
    i = [9, 3, 15, 20, 7]
    t = construct_optimized(p, i)
    assert t.val == 3
    assert t.left.val == 9
    assert t.right.val == 20
    assert t.right.left.val == 15
    assert t.right.right.val == 7

    t = construct([-1], [-1])
    assert t.val == -1


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
