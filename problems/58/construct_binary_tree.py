class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct(preorder: list[int], inorder: list[int]) -> TreeNode:
    if not preorder:
        return None
    if len(preorder) == 1:
        return TreeNode(preorder[0])

    root = preorder[0]

    # TODO: use a dict to store the indexes of inorder for
    # quicker lookup. Don't do slicing but passing in start/end
    # indexes so that the dictionary only needs to be initialized
    # once on the first time seeing the inorder list.
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
    t = construct(p, i)
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
    t = construct(p, i)
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
