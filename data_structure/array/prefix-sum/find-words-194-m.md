# Find Words 194 (M)

## Problem

Given a string `str` and a dictionary `dict`, you need to find out which words in the dictionary are subsequences of the string and return those words.The order of the words returned should be the same as the order in the dictionary.

1. |str|<=1000
2. the sum of all words length in dictionary<=1000

(All characters are in lowercase)Example

Example 1:

```
Input:str="bcogtadsjofisdhklasdj"dict=["book","code","tag"]Output:["book"]Explanation:Only book is a subsequence of str
```

Example 2:

```
Input:str="nmownhiterer"dict=["nowhere","monitor","moniter"]Output:["nowhere","moniter"]
```

Challenge

|str|<=100000

## Solution - Brute Force

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param str: the string
    @param dict: the dictionary
    @return: return words which  are subsequences of the string
    """
    def findWords(self, str, dict):
        # write your code here.
        res = []
        if not str or not dict:
            return res
        
        for word in dict:
            i, j = 0, 0
            while i < len(str) and j < len(word):
                if str[i] == word[j]:
                    i+=1
                    j+=1
                elif str[i] != word[j]:
                    i+=1
                if j == len(word):
                    res.append(word)
        return res
                
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n \* m)**
  * n: len(str)
  * m: len(dict)
* **Space Complexity:**



## Solution - Prefix Dict + Two Pointer

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param str: the string
    @param dict: the dictionary
    @return: return words which  are subsequences of the string
    """
    def findWords(self, str, dict):
        # write your code here.
        ans = []
        n = len(str)

        nxt_pos = [[n for i in range(26)] for j in range(n + 1)]

        # nxt_pos[i][j]: for s[i:], the next position of j in s
        for i in range(n - 1, -1, -1):
            for j in range(26):
                nxt_pos[i][j] = nxt_pos[i + 1][j]
                if ord(str[i]) - ord('a') == j:
                    nxt_pos[i][j] = i
        print(nxt_pos)
        
        
        for word in dict:
            i = 0
            j = 0
            m = len(word)
            while i < n + 1 and j < m:
                i = nxt_pos[i][ord(word[j]) - ord('a')] + 1
                if i != n + 1:
                    j +=1
                if j == m:
                    ans.append(word)
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(26n)**
  * n: len(str)
* **Space Complexity: O(n)**
