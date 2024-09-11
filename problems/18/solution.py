from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    left = None
    right = head

    while right:
        tmp = right.next
        right.next = left
        left, right = right, tmp

    return left


def reverse_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    return _reverse(None, head)

def _reverse(left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
    if not right:
        return left

    new_head = _reverse(right, right.next)
    right.next = left
    return new_head


def test_reverse():
    output = reverse(ListNode(1, ListNode(2)))
    assert output.val == 2 and output.next.val == 1

    output = reverse_recursive(ListNode(1, ListNode(2)))
    assert output.val == 2 and output.next.val == 1

    for output in [
        reverse(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))),
        reverse_recursive(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))),
    ]:
        n = output
        expected = 5
        while n:
            assert n.val == expected
            expected -= 1
            n = n.next

    assert reverse(None) == None
    assert reverse_recursive(None) == None


if __name__ == "__main__":
    import pytest
    pytest.main(["-xvv", __file__])
