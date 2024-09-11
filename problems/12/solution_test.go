package main

import (
	"testing"
)

type input struct {
	list     *ListNode
	expected bool
}

func GetInputs() []input {
	list1 := &ListNode{Val: 3}
	list1.Next = &ListNode{Val: 2}
	list1.Next.Next = &ListNode{Val: 0}
	list1.Next.Next.Next = &ListNode{Val: 4}
	list1.Next.Next.Next.Next = list1.Next // Cycle

	list2 := &ListNode{Val: 1}
	list2.Next = &ListNode{Val: 2}
	list2.Next.Next = list2 // cycle

	list3 := &ListNode{Val: 1}

	return []input{
		{list1, true},
		{list2, true},
		{list3, false},
		{nil, false},
	}
}

func TestIsCycle(t *testing.T) {
	for _, input := range GetInputs() {
		if IsCycle(input.list) != input.expected {
			t.Fail()
		}
	}
}

func TestIsCycleConstantMemory(t *testing.T) {
	for _, input := range GetInputs() {
		if IsCycleConstantMemory(input.list) != input.expected {
			t.Fail()
		}
	}
}
