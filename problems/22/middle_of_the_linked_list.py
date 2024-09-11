from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_simple(ll: Optional[ListNode]) -> Optional[ListNode]:
    """
    Return the middle node in a linked list by converting it to an
    indexable list in Python and return the middle element.
    """
    unlinked = []
    while ll:
        unlinked.append(ll.val)
        ll = ll.next

    return unlinked[len(unlinked) // 2]

def middle(ll: Optional[ListNode]) -> Optional[ListNode]:
    """
    Return the middle node in a linked list using the fast/slow
    pointer method.
    """
    if ll.next == None:
        return ll

    fast = ll
    slow = ll
    while True:
        if not fast or not fast.next:
            return slow

        slow = slow.next
        fast = fast.next.next


def test_middle():
    nodes = [ListNode(n) for n in range(1, 6)]
    for left, right in zip(nodes[:], nodes[1:]):
        left.next = right

    ll = nodes[0]
    assert ll.val == 1 and ll.next.val == 2 and ll.next.next.val == 3
    assert not ll.next.next.next.next.next

    # test that we get 3
    assert middle(nodes[0]).val == 3
    assert middle_simple(nodes[0]) == 3

    # add a 6th node, make sure we get 4
    nodes[-1].next = ListNode(6)
    assert middle(nodes[0]).val == 4
    assert middle_simple(nodes[0]) == 4


if __name__ == "__main__":
    import pytest
    pytest.main(["-xvv", __file__])
