# Palindrome Partitioning 136 \(M\)

## Problem

Given a string `s`. Partition `s` such that every substring in the partition is a palindrome.

Return all possible palindrome partitioning of `s`.

1. Different partitionings can be in any order.
2. Each substring must be a continuous segment of `s`.

Example

**Example 1:**

```text
Input: "a"
Output: [["a"]]
Explanation: Only 1 char in the string, only 1 way to split it (itself).
```

**Example 2:**

```text
Input: "aab"
Output: [["aa", "b"], ["a", "a", "b"]]
Explanation: There are 2 ways to split "aab".
    1. Split "aab" into "aa" and "b", both palindrome.
    2. Split "aab" into "a", "a", and "b", all palindrome.
```

## Solution - DFS + Memoization

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        res = []
        if not s:
            return res
        self.dfs(0, s, [], {}, res)
        return res
    
    def dfs(self, index, s, path, memo, res):
        if index == len(s):
            res.append(path[:])
            return 
        for i in range(index, len(s)):
            substr = s[index : i + 1]
            if not self.is_palindrome(substr, memo):
                continue
            path.append(substr)
            self.dfs(i + 1, s, path, memo, res)
            path.pop()
    
    def is_palindrome(self, substr, memo):
        if substr in memo:
            return memo[substr]
        start, end = 0, len(substr) - 1
        while start < end:
            if substr[start] != substr[end]:
                memo[substr] = False
                return False
            else:
                start+=1
                end-=1
        memo[substr] = True
        return True
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

