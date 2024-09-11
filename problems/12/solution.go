package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func IsCycle(node *ListNode) bool {
	if node == nil {
		return false
	}

	visited := make(map[*ListNode]bool)
	for current := node; current != nil; current = current.Next {
		_, found := visited[current]
		if found {
			return true
		}
		visited[current] = true
	}
	return false
}

func IsCycleConstantMemory(node *ListNode) bool {
	if node == nil {
		return false
	}

	slow := node
	fast := node.Next
	for slow != nil && fast != nil {
		if slow == fast {
			return true
		}

		// increment pointers
		slow = slow.Next
		fast = fast.Next
		if fast != nil {
			fast = fast.Next
		}
	}

	return false
}
