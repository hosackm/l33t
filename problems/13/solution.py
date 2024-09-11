class Stack:
    def __init__(self):
        self.data = []

    def empty(self) -> bool:
        return len(self.data) == 0

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        return self.data.pop(-1)

    def peek(self) -> int:
        return self.data[-1]


class MyQueue:
    def __init__(self):
        self.stack = Stack()
        self.holding = Stack()

    def push(self, x: int) -> None:
        self.stack.push(x)

    def pop(self) -> int:
        self._swap(self.stack, self.holding)
        result = self.holding.pop()
        self._swap(self.holding, self.stack)

        return result

    def peek(self) -> int:
        self._swap(self.stack, self.holding)
        result = self.holding.peek()
        self._swap(self.holding, self.stack)

        return result

    def empty(self) -> bool:
        return self.stack.empty()

    def _swap(self, a, b):
        while not a.empty():
            b.push(a.pop())


def test_queue():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() == False


def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    assert s.empty() == False
    assert s.peek() == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.empty() == True


if __name__ == "__main__":
    import pytest
    pytest.main(["-xvv", __file__])
