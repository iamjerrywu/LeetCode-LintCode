# Number of Strings That Appear as Substrings in Word (LeetCode 1967) (E)

## Problem

Given an array of strings `patterns` and a string `word`, return _the **number** of strings in _`patterns`_ that exist as a **substring** in _`word`.

A **substring** is a contiguous sequence of characters within a string.

**Example 1:**

```
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.
```

**Example 2:**

```
Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
Output: 2
Explanation:
- "a" appears as a substring in "aaaaabbbbb".
- "b" appears as a substring in "aaaaabbbbb".
- "c" does not appear as a substring in "aaaaabbbbb".
2 of the strings in patterns appear as a substring in word.
```

**Example 3:**

```
Input: patterns = ["a","a","a"], word = "ab"
Output: 3
Explanation: Each of the patterns appears as a substring in word "ab".
```

**Constraints:**

* `1 <= patterns.length <= 100`
* `1 <= patterns[i].length <= 100`
* `1 <= word.length <= 100`
* `patterns[i]` and `word` consist of lowercase English letters.

## Solution - String.Find()

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for pattern in patterns:
            if word.find(pattern) != -1:
                ans+=1
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - Construct Substrings (1)

Count the substring with start, and the end point

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        substrings = self.build_substrings(word)
        ans = 0
        for pattern in patterns:
            if pattern in substrings:
                ans+=1
        return ans
    def build_substrings(self, word):
        substrings = set()
        for length in range(1, len(word) + 1):
            for start in range(len(word) - length + 1):
                substrings.add(word[start:start + length])
        return substrings
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution - Construct Substrings (2)

Count the substring with start, and the length of substrings

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        substrings = self.build_substrings(word)
        ans = 0
        for pattern in patterns:
            if pattern in substrings:
                ans+=1
        return ans
    
    def build_substrings(self, word):
        substrings = set()
        for start in range(len(word)):
            for end in range(start, len(word) + 1): 
            # if write like following, would not count "" as substring
            # for end in range(start + 1, len(word) + 1): 
                substrings.add(word[start:end])
        return substrings
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
