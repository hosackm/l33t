class Trie:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_terminal = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = self.Node()
            node = node.children[ch]
        node.is_terminal = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return node.is_terminal

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


def test_trie():
    t = Trie()
    t.insert("apple")
    assert t.search("apple") == True
    assert t.search("app") == False
    assert t.startsWith("app") == True
    t.insert("app")
    assert t.search("app") == True


if __name__ == "__main__":
    import pytest

    pytest.main(["-xvv", __file__])
