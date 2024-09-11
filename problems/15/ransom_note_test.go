package main

import (
	"testing"
)

func TestCanConstruct(t *testing.T) {
	inputs := [][2]string{
		{"a", "b"},
		{"aa", "ab"},
		{"aa", "aab"},
	}
	outputs := []bool{false, false, true}

	for i, input := range inputs {
		if CanConstruct(input[0], input[1]) != outputs[i] {
			t.Fail()
		}
	}
}
