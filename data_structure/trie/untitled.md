# Implement Trie (Prefix Tree) 442 (M)

## Problem

Implement a Trie with `insert`, `search`, and `startsWith` methods.

You may assume that all inputs are consist of lowercase letters a-z.Example

**Example 1:**

```
Input:  insert("lintcode")  search("lint")  startsWith("lint")Output:  false  true
```

**Example 2:**

```
Input:  insert("lintcode")  search("code")  startsWith("lint")  startsWith("linterror")  insert("linterror")  search("lintcode“)  startsWith("linterror")Output:  false  true  false  true  true
```

## Solution&#x20;

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

{% tab title="C++" %}
````cpp
class TrieNode {
public:
    map<char, TrieNode*> children;
    bool is_word = false;
};

class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode;
            }
            node = node->children[c];
        }
        node->is_word = true;
    }
    
    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) return false;
            node = node->children[c];
        }
        return node->is_word;
    }
    
    bool startsWith(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (!node->children.count(c)) return false;
            node = node->children[c];
        }
        return true;
        
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
```
````
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
  * insert(): O(L)
  * has\_word(): O(L)
  * startWith(): O(L)
* **Space Complexity: O(L)**
