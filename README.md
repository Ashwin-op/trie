# Trie

This is an implementation of a Trie data structure in Python. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to store the entire English language for quick prefix lookups.

This repository also contains the implementation of Suffix Trees. Everything is implemented in [trie.py](trie.py).

## Variants

1. Uncompressed Trie - This is the simplest form of a trie. It is not space-efficient as it stores a lot of redundant information.
2. Compressed Trie - This is a more space-efficient version of a trie. It compresses the trie by merging nodes with a single child into a single node.
3. Uncompressed Suffix Tree - This is the simplest form of a suffix tree. It is not space-efficient as it stores a lot of redundant information.
4. Compressed Suffix Tree - This is a more space-efficient version of a suffix tree. It compresses the suffix tree by merging nodes with a single child into a single node.

## Usage

```python
from trie import Trie

# Create a new trie
trie = Trie() # or Trie(is_compressed=True) for a compressed trie

# Insert a word into the trie
trie.insert("hello")
trie.insert("world")

# Search for a word in the trie
trie.search("hello") # 5 (depth of the word in the trie)
```
