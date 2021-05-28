# Generate Parenthese 427 \(M\)

## Problem

Given n, and there are n pairs of parentheses, write a function to generate all combinations of well-formed parentheses, And return the combination result.Example

**Example 1:**

```text
Input: 3Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

**Example 2:**

```text
Input: 2Output: ["()()", "(())"]
```

## Solution - DFS \(1\)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        res = []
        self.dfs(n, [], 0, res)
        return res
    
    def dfs(self, n, sequence, left_paren, res):
        if len(sequence) == 2 * n:
            res.append(''.join(sequence))
            return 
        if left_paren < n:
            sequence.append('(')
            self.dfs(n, sequence, left_paren + 1, res)
            sequence.pop()
        # can only add ')' if the amount of ')' is less then '('
        if left_paren > len(sequence) - left_paren:
            sequence.append(')')
            self.dfs(n, sequence, left_paren, res)
            sequence.pop()
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

## Solution - DFS \(2\)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        res = []
        self.dfs(n, [], 0, res)
        return res
    
    def dfs(self, n, sequence, left_paren, res):
        if len(sequence) == 2 * n:
            res.append(''.join(sequence))
            return 
        if left_paren < n:
            sequence.append('(')
            self.dfs(n, sequence, left_paren + 1, res)
            sequence.pop()
        # can only add ')' if the amount of ')' is less then '('
        if left_paren > len(sequence) - left_paren:
            sequence.append(')')
            self.dfs(n, sequence, left_paren, res)
            sequence.pop()
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

