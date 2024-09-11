from solution import merge, ListNode


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
