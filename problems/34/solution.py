from collections import defaultdict as dd


def can_finish(num_courses: int, prereqs: list[list[int]]) -> bool:
    graph = dd(list)
    for pre in prereqs:
        # before, goal = pre
        goal, before = pre
        graph[goal].append(before)

    for v in graph:
        if is_cycle(graph, v):
            return False
        graph[v] = []
    return True


def is_cycle(g, v):
    """
    Returns True if there is a cycle from v to itself
    by passing through the edges in g.
    """
    queue = list(g[v])
    visited = set()
    while queue:
        current = queue.pop()
        if current in visited:
            return True

        visited.add(current)
        for e in g.copy()[current]:
            queue.append(e)

    return False


def test_can_finish():
    assert can_finish(2, [[0, 1]]) == True
    assert can_finish(2, [[0, 1], [1, 0]]) == False


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
