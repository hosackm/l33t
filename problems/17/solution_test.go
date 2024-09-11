package main

import (
	"testing"
)

func TestLongestPalindrome(t *testing.T) {
	if LongestPalindrome("abccccdd") != 7 {
		t.Fail()
	}
	if LongestPalindrome("a") != 1 {
		t.Fail()
	}
}
