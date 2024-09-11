package main

const StackSize = 500

type Stack struct {
	items [StackSize]int
	index int
}

func NewStack() *Stack {
	return &Stack{index: -1}
}

func (s *Stack) Push(val int) {
	s.index++
	s.items[s.index] = val
}

func (s *Stack) Peek() int {
	return s.items[s.index]
}

func (s *Stack) Pop() int {
	val := s.items[s.index]
	s.index--
	return val
}

func (s *Stack) IsEmpty() bool {
	return s.index == -1
}

type MyQueue struct {
	main *Stack
	aux  *Stack
}

func NewQueue() *MyQueue {
	return &MyQueue{
		main: NewStack(),
		aux:  NewStack(),
	}
}

func (m *MyQueue) Push(val int) {
	m.main.Push(val)
}

func (m *MyQueue) Peek() int {
	m.Swap(MainToAux)
	result := m.aux.Peek()
	m.Swap(AuxToMain)
	return result
}

func (m *MyQueue) Pop() int {
	m.Swap(MainToAux)
	result := m.aux.Pop()
	m.Swap(AuxToMain)
	return result
}

func (m *MyQueue) IsEmpty() bool {
	return m.main.IsEmpty()
}

const (
	MainToAux = 0
	AuxToMain = 1
)

func (m *MyQueue) Swap(direction int) {
	switch direction {
	case MainToAux:
		for !m.main.IsEmpty() {
			m.aux.Push(m.main.Pop())
		}
	case AuxToMain:
		for !m.aux.IsEmpty() {
			m.main.Push(m.aux.Pop())
		}
	}
}
