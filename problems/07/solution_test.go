package main

import (
	"testing"
)

func TestIsAnagram(t *testing.T) {
	inputs := []struct {
		s        string
		t        string
		expected bool
	}{
		{"", "", true},
		{"", "a", false},
		{"anagram", "nagaram", true},
		{"rat", "car", false},
	}

	for _, input := range inputs {
		result := IsAnagram(input.s, input.t)
		if result != input.expected {
			t.Errorf("'%s' -> '%s', expected %#v, got %#v", input.s, input.t, input.expected, result)
		}
	}
}
