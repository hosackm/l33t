package main

import (
	"testing"
)

func TestMaxProfit(t *testing.T) {
	inputs := [][]int{
		{7, 1, 5, 3, 6, 4},
		{7, 6, 4, 3, 1},
		{},
		{1},
		{1, 0},
	}
	outputs := []int{5, 0, 0, 0, 0}
	for i, input := range inputs {
		got := MaxProfit(input)
		if got != outputs[i] {
			t.Errorf("got: %d, expected %d", got, outputs[i])
		}
	}
}
