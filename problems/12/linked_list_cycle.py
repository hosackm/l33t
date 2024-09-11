from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def is_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect cycles by walking two pointers through a linked list
    if they arrive at the same node at the same time then there must be
    a cycle. Uses constant memory but takes linear time.
    """
    if not head:
        return False

    slow = head
    fast = head.next if head.next else None
    while slow and fast:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next if fast.next else None
    return False

def is_cycle_2(head: Optional[ListNode]) -> bool:
    """
    Solve by tracking visited nodes and if we land on a visited node
    we know there's a cycle. Takes linear amount of memory.
    """
    # count nodes, fill map of nodes being pointed to
    visited = set()
    current = head
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False


def test_is_cycle_example_1():
    ln = ListNode(3)
    ln.next = ListNode(2)
    ln.next.next = ListNode(0)
    ln.next.next.next = ListNode(4)
    ln.next.next.next = ln.next  # cycle
    assert is_cycle(ln) == True
    assert is_cycle_2(ln) == True


def test_is_cycle_example_2():
    ln = ListNode(1)
    ln.next = ListNode(2)
    ln.next.next = ln  # cycle
    assert is_cycle(ln) == True
    assert is_cycle_2(ln) == True


def test_is_cycle_example_3():
    ln = ListNode(1)
    assert is_cycle(ln) == False
    assert is_cycle_2(ln) == False


if __name__ == "__main__":
    import pytest
    pytest.main(["-xvv", __file__])
