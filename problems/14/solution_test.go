package main

import (
	"testing"
)

func TestFindBad(t *testing.T) {
	if FindBad(5, func(x int) bool { return x >= 4 }) != 4 {
		t.Fail()
	}
	if FindBad(1, func(x int) bool { return true }) != 1 {
		t.Fail()
	}
}
