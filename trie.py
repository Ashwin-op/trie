# explanations for member functions are provided in requirements.py
# each file that uses a skip list should import it from this file.

from typing import List


class Node:
    def __init__(self, key: str = ""):
        self.key = key
        self.children = {}
        self.end_of_string = False

    def __str__(self):
        return f"Node({self.key}, {self.end_of_string})"

    def __repr__(self):
        return f"Node({self.key}, {[repr(child) for child in self.children.values()]}, {self.end_of_string})"


class Trie:
    def __init__(self, is_compressed: bool):
        self.is_compressed = is_compressed
        self.root = Node()

    def construct_trie_from_text(self, keys: List[str]) -> None:
        for key in keys:
            self._insert(key)

        if self.is_compressed:
            self._compress(self.root)

    def construct_suffix_tree_from_text(self, keys: List[str]) -> None:
        for key in keys:
            for i in range(len(key)):
                self._insert(key[i:])

        if self.is_compressed:
            self._compress(self.root)

    def _insert(self, key: str) -> None:
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
        node.end_of_string = True

    def _compress(self, node: Node) -> None:
        if len(node.children) == 0:
            return
        if len(node.children) == 1 and not node.end_of_string and node != self.root:
            child = list(node.children.values())[0]
            node.key += child.key
            node.children = child.children
            node.end_of_string = child.end_of_string
            self._compress(node)
        else:
            for child in node.children.values():
                self._compress(child)

    def search_and_get_depth(self, key: str) -> int:
        result = ""
        node = self.root
        depth = 0
        i = 0
        while i < len(key):
            char = key[i]
            if char in node.children:
                node = node.children[char]
                result += node.key
                i += len(node.key)
                depth += 1
            else:
                return -1
        return depth if node.end_of_string and result == key else -1


# feel free to define new classes/methods in addition to the above
# fill in the definitions of each required member function (above),
# and any additional member functions you define
