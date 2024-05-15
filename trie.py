class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isend = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    # NOTE: runs in async 
    async def fill(self, words: list[str]) -> None:
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isend = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isend

    def starts_with(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

    def complete(self, prefix: str) -> list[str]:
        cur = self.root
        result = []
        for c in prefix:
            if c not in cur.children:
                return result
            cur = cur.children[c]

        def dfs(node: TrieNode, cur_word: str) -> None:
            if node.isend:
                result.append(cur_word)

            for child, child_node in node.children.items():
                dfs(child_node, cur_word + child)

        dfs(cur, prefix)
        return result
