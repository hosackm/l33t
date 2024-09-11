package main

import (
	"testing"
)

func TestFloodFill(t *testing.T) {
	img := [][]int{
		{1, 1, 1},
		{1, 1, 0},
		{1, 0, 1},
	}
	expected := [][]int{
		{2, 2, 2},
		{2, 2, 0},
		{2, 0, 1},
	}

	result := FloodFill(img, 1, 1, 2)
	for i := range result {
		for j := range result[i] {
			if result[i][j] != expected[i][j] {
				t.Fail()
			}
		}
	}
}
