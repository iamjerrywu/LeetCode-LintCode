# Implement Trie \(Prefix Tree\) 442 \(M\)

## Problem

Implement a Trie with `insert`, `search`, and `startsWith` methods.

You may assume that all inputs are consist of lowercase letters a-z.Example

**Example 1:**

```text
Input:  insert("lintcode")  search("lint")  startsWith("lint")Output:  false  true
```

**Example 2:**

```text
Input:  insert("lintcode")  search("code")  startsWith("lint")  startsWith("linterror")  insert("linterror")  search("lintcode“)  startsWith("linterror")Output:  false  true  false  true  true
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    
    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_word = True
        node.word = word

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        # there must be word eventually start with this prefix
        return True
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
  * insert\(\): O\(L\)
  * has\_word\(\): O\(L\)
  * startWith\(\): O\(L\)
* **Space Complexity: O\(L\)**

