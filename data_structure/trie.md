# Trie

## What's Trie?

It's a data structure that accelerates in solving graph word search problems, faster than simply using hashmap. 

For example, we add word "abc", and search ".bc", "a..", these should all give as `True` 

If using hashmap we need to store 26^3 of possibilities, and mark all the ones that can be found as `True`, while others as `False` Apparently, that's a huge space complexity we required, therefore we need to use a better approach.

 Trie is like a prefix tree, is a type of search tree, a tree **data structure** used for locating specific keys from within a set. 

## Template:



```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def get_root(self):
        return self.root
    
    def insert(self, word):
        node = self.root
        # traverse word
        for i in range(len(word)):
            if word[i] not in node.children:
                # if child not exist that char, need to init new child node
                node.children[word[i]] = TrieNode()
            # point to current char
            node = node.children[word[i]]
        # since we insert a valid vocabulary, should update is_word and word, when reaching the last node
        node.is_word = True
        node.word = word
```

