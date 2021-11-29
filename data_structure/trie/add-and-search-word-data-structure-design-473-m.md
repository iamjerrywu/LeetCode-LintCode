# Add and Search Word - Data structure design 473 (M)

## Problem

Design a data structure that supports the following two operations: `addWord(word)` and `search(word)`

Addword (word) adds a word to the data structure.`search(word)` can search a literal word or a regular expression string containing only letters `a-z` or `.`.

A `.` means it can represent any one letter.

You may assume that all words are consist of lowercase letters a-z.Example

**Example 1:**

```
Input:  addWord("a")  search(".")Output:  true
```

**Example 2:**

```
Input:  addWord("bad")  addWord("dad")  addWord("mad")  search("pad")    search("bad")    search(".ad")    search("b..")  Output:  false  true  true  true
```

## Solution - Set

### Code

{% tabs %}
{% tab title="python" %}
```python
class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def __init__(self):
        self.ref = collections.defaultdict(set)

    def addWord(self, word):
        # write your code here
        self.ref[len(word)].add(word)

        

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        n = len(word)
        for ref_word in self.ref[n]:
            same_cnt = 0
            for i in range(n):
                if word[i] == '.' or word[i] == ref_word[i]:
                    same_cnt+=1
            if same_cnt == n:
                return True
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**&#x20;
  * addword(): O(1)
  * Search():  O(m \* n)
    * m: length-n word's amount
    * n: length of the word
* **Space Complexity: O(n)**

****

## Solution - Trie (Complete)

Construct Trie Node data structure&#x20;

### Code

{% tabs %}
{% tab title="python" %}
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
    

class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word):
        # write your code here
        self.trie.insert(word)

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        return self.dfs(self.trie.get_root(), word, 0)
    
    def dfs(self, root, word, index):
        if index == len(word):
            return root.is_word
        letter = word[index]
        if letter == '.':
            for child in root.children:
                if self.dfs(root.children[child], word, index + 1):
                    return True
            return False
        # if not '.'
        if letter in root.children:
            return self.dfs(root.children[letter], word, index + 1)
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
  * addword(): O(n)
  * Search:&#x20;
    * Best Case: O(n), n is the word length
    * Worst Case: need to traverse the whole trie O(26^n \* m)
      * n is the word length
      * m is the number of keys
* **Space Complexity:**
  * addword(): O(n)

## Solution - Trie(Simple)

Construct trie in a simpler way

### Code

{% tabs %}
{% tab title="python" %}
```python
class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        # write your code here
        node = self.trie

        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['$'] = True
        

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        return self.dfs(self.trie, word, 0)
    
    def dfs(self, node, word, index):
        if index == len(word):
            return node.get('$', False)
        
        letter = word[index]
        if letter == '.':
            for child in node:
                if child != '$' and self.dfs(node[child], word, index + 1):
                    return True
            return False
        # if not '.'
        if letter in node:
            return self.dfs(node[letter], word, index + 1)
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
  * addword(): O(n)
  * Search:&#x20;
    * Best Case: O(n), n is the word length
    * Worst Case: need to traverse the whole trie O(26^n \* m)
      * n is the word length
      * m is the number of keys
* **Space Complexity:**
  * addword(): O(n)
