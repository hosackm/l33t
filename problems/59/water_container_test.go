package main

import (
	"testing"
)

func TestWaterContainer(t *testing.T) {
	inputs := []struct {
		nums     []int
		expected int
	}{
		{[]int{1, 8, 6, 2, 5, 4, 8, 3, 7}, 49},
		{[]int{1, 1}, 1},
		{[]int{1, 2, 4, 3}, 4},
		{[]int{2, 3, 4, 5, 18, 17, 6}, 17},
		{[]int{1, 0, 0, 0, 0, 0, 0, 2, 2}, 8},
	}
	for _, input := range inputs {
		if MaxArea(input.nums) != input.expected {
			t.Fail()
		}
	}
}
