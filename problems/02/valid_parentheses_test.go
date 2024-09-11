package main

import (
	"testing"
)

func TestValidParens(t *testing.T) {
	inputs := []string{
		"()",
		"()[]{}",
		"(]",
	}
	outputs := []bool{true, true, false}
	for i, input := range inputs {
		output := ValidParentheses(input)
		if output != outputs[i] {
			t.Errorf("got %#v but expected %#v\n", output, outputs[i])
		}
	}
}
