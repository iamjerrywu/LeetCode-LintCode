# Shortest Word Distance (LeetCode 243) (E)

## Problem

Given an array of strings `wordsDict` and two different strings that already exist in the array `word1` and `word2`, return _the shortest distance between these two words in the list_.

**Example 1:**

```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
```

**Example 2:**

```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
```

**Constraints:**

* `1 <= wordsDict.length <= 3 * 104`
* `1 <= wordsDict[i].length <= 10`
* `wordsDict[i]` consists of lowercase English letters.
* `word1` and `word2` are in `wordsDict`.
* `word1 != word2`

## Solution&#x20;



{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        appear = []
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                appear.append([1, i])
            if wordsDict[i] == word2:
                appear.append([2, i])
        
        ans = float('inf')
        
        for i in range(len(appear) - 1):
            if appear[i][0] != appear[i + 1][0]:
                ans = min(ans, appear[i + 1][1] - appear[i][1])
        return ans
```
{% endtab %}
{% endtabs %}

* **Time Complexity: **
* **Space Complexity: **
