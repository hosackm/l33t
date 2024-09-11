package main

import (
	"testing"
)

func TestBinarySearch(t *testing.T) {
	inputs := []struct {
		nums     []int
		target   int
		expected int
	}{
		{[]int{-1, 0, 3, 5, 9, 12}, 9, 4},
		{[]int{-1, 0, 3, 5, 9, 12}, 2, -1},
		{[]int{5}, 5, 0},
	}

	for _, input := range inputs {
		result := BinarySearch(input.nums, input.target)
		if result != input.expected {
			t.Errorf(
				"binary search %#v -> %d, got %d, expected %d",
				input.nums,
				input.target,
				result,
				input.expected,
			)
		}
	}
}
