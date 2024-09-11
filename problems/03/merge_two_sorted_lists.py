class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def merge(first: ListNode | None, second: ListNode | None) -> ListNode | None:
    answer = ListNode(0)
    write = answer

    while first and second:
        if first.val < second.val:
            write.next = first
            first = first.next
        else:
            write.next = second
            second = second.next
        write = write.next

    # process leftovers
    if first:
        write.next = first
    if second:
        write.next = second

    return answer.next


def test_merge_lists():
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    output = merge(list1, list2)

    i = 0
    expected = [1, 1, 2, 3, 4, 4]
    head = output
    while head:
        assert head.val == expected[i]
        i += 1
        head = head.next

    list1 = None
    list2 = None
    output = merge(list1, list2)
    assert output is None

    list1 = None
    list2 = ListNode(0)
    output = merge(list1, list2)
    assert output.val == 0


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
