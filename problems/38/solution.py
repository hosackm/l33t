class Stack:
    def __init__(self):
        self.data = []

    def peek(self):
        return self.data[-1]

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0


class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.mins = Stack()

    def push(self, val: int) -> None:
        self.stack.push(val)
        if self.mins.is_empty() or val <= self.mins.peek():
            self.mins.push(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.mins.peek():
            self.mins.pop()
        return popped

    def top(self) -> int:
        return self.stack.peek()

    def getMin(self) -> int:
        return self.mins.peek()


def test_min_stack():
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
