import operator


operands = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
}


def eval_rpn(tokens: list[str]) -> int:
    stack = []
    for tk in tokens:
        func = operands.get(tk)
        if func is None:
            stack.append(int(tk))
            continue

        op2 = stack.pop()
        op1 = stack.pop()
        stack.append(int(func(op1, op2)))

    return stack.pop()


def test_eval_rpn():
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
    expr = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert eval_rpn(expr) == 22


def test_operands():
    assert len(operands) == 4


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
