import pytest


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


def clone_graph(node: Optional["Node"]) -> Optional["Node"]:
    if not node:
        return node

    table = {}
    queue = [node]
    visited = set()

    while queue:
        n = queue.pop(0)
        if n.val in visited:
            continue

        visited.add(n.val)
        table[n.val] = n.neighbors

        for ngb in n.neighbors:
            queue.append(ngb)

    # nodes = [Node(n, []) for n in table.keys()]
    nodes = [Node(n + 1, []) for n in range(len(table))]
    for i in range(1, len(table) + 1):
        for ngbs in table.get(i):
            nodes[i].neighbors.append(nodes[ngbs.val - 1])

    return nodes[0]


def create_graph(adj):
    nodes = []
    neighbors = []

    for i, a in enumerate(adj):
        nodes.append(Node(i, []))
        neighbors.append(a)

    for i, nbs in enumerate(neighbors):
        for nb in nbs:
            nodes[i].neighbors.append(nodes[nb - 1])

    return nodes[0] if nodes else []


@pytest.mark.skip()
def test_create_graph():
    adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
    g = create_graph(adj_list)
    assert g.val == 1
    for nb in g.neighbors:
        assert isinstance(nb, Node)


@pytest.mark.skip()
def test_clone_graph():
    adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
    g = create_graph(adj_list)

    gc = clone_graph(g)

    assert g.val == 1
    assert g.neighbors == [2, 4]
    assert g is not gc


if __name__ == "__main__":
    pytest.main(["-xvv", __file__])
