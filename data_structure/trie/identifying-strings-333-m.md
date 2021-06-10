# Identifying Strings 333 \(M\)

## Problem

Given n character strings containing only lower case letters, find the minimum prefix strings that can identify each string.  
That is, the minimum prefix string Ap which identifies string A will not be a prefix string of other n-1 character strings.

1 &lt;= n &lt;= 500  
The length of strings would not exceed 100.  
If string S is a profix of string T, the answer of S will be itself.Example

Input:\["aaa","bbc","bcd"\]  
Output:\["a","bb","bc"\]  
Explanation:"a" is only the profix of "aaa".  
"bb" is only the profix of "bbc".  
"bc" is only the profix of "bcd".

## Solution - Brute Force Enumeration

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param stringArray: a string array
    @return: return every strings'short peifix
    """
    def ShortPerfix(self, stringArray):
        # write your code here
        prefix_sum_cnt = self.get_prefix_sum_cnt(stringArray)
        res = []
        for string in stringArray:
            cur_string = ''
            for i in range(len(string)):
                cur_string = string[:i + 1]
                if prefix_sum_cnt[cur_string] == 1 or i == len(string) - 1:
                    res.append(cur_string)
                    break
        return res
    
    def get_prefix_sum_cnt(self, stringArray):
        prefix_sum_cnt = {}
        for string in stringArray:
            cur_string = ''
            for i in range(len(string)):
                cur_string = string[:i + 1]
                prefix_sum_cnt[cur_string] = prefix_sum_cnt.get(cur_string, 0) + 1
        return prefix_sum_cnt
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n \* \(L^2\)\)**
  * n: len\(stringArray\)
  * get cur\_string: O\(L\)
  * traverse char n string: O\(L\)
* **Space Complexity: O\(n \* L\)**

## Solution - Trie

### Code

{% tabs %}
{% tab title="python" %}
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def get_root(self):
        return self.root
    
    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
            node.prefix_count+=1
        node.is_word = True
        node.word = word

class Solution:
    """
    @param stringArray: a string array
    @return: return every strings'short peifix
    """
    def ShortPerfix(self, stringArray):
        # write your code here
        trie = Trie()
        res = []
        for word in stringArray:
            trie.insert(word)
        for word in stringArray:
            res.append(self.get_unique_prefix(trie.get_root(), word))
        return res
    
    def get_unique_prefix(self, root, word):
        node = root
        for i in range(len(word)):
            if node.prefix_count == 1:
                # when i = 0, node.prefix_count = 0  
                # when i = 1, node.prefix_count = 1, then word[:i] = word[0]
                return word[:i]
            node = node.children[word[i]]
        return word
    


```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n \* \(L^2\)\)**
  * n: len\(stringArray\)
  * get cur\_string: O\(L\)
  * traverse char n string: O\(L\)
* **Space Complexity: O\(n \* L\)**

