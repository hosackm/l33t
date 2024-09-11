package main

import (
	"testing"
)

func TestStack(t *testing.T) {
	s := NewStack()

	if !s.IsEmpty() {
		t.Fail()
	}

	s.Push(1)
	s.Push(2)

	if s.Peek() != 2 {
		t.Fail()
	}
	if s.IsEmpty() {
		t.Fail()
	}

	if s.Pop() != 2 {
		t.Fail()
	}
	if s.Pop() != 1 {
		t.Fail()
	}

	if !s.IsEmpty() {
		t.Fail()
	}
}

func TestQueue(t *testing.T) {
	q := NewQueue()
	if !q.IsEmpty() {
		t.Fail()
	}

	q.Push(1)
	q.Push(2)

	if q.IsEmpty() {
		t.Fail()
	}

	if q.Peek() != 1 {
		t.Fail()
	}
	if q.Pop() != 1 {
		t.Fail()
	}
	if q.Pop() != 2 {
		t.Fail()
	}

	if !q.IsEmpty() {
		t.Fail()
	}
}
