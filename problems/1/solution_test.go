package main

import (
	"testing"
)

func TestTwoSum(t *testing.T) {
	inputs := []struct {
		nums     []int
		target   int
		expected []int
	}{
		{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
		{[]int{3, 2, 4}, 6, []int{1, 2}},
		{[]int{3, 3}, 6, []int{0, 1}},
	}

	for _, input := range inputs {
		indexes := TwoSum(input.nums, input.target)
		for i, index := range indexes {
			if index != input.expected[i] {
				t.Errorf("Answer didn't match. Got %d expected %d", index, input.expected[i])
			}
		}
	}
}
