class Trie:
    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        if not word:
            return
        node = self.tree
        for char in word:
            node = node.setdefault(char, {})
        node["#"] = 1

    def search(self, word: str) -> bool:
        node = self.tree
        for char in word:
            node = node.get(char)
            if not node:
                return False
        return "#" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.tree
        for char in prefix:
            node = node.get(char)
            if not node:
                return False
        return True

