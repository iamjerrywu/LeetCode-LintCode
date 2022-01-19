# Generate Parenthese 427 (M)

## Problem

Given n, and there are n pairs of parentheses, write a function to generate all combinations of well-formed parentheses, And return the combination result.Example

**Example 1:**

```
Input: 3Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

**Example 2:**

```
Input: 2Output: ["()()", "(())"]
```

## Solution - DFS (1)

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

****

## Solution - DFS (2)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left, right = n, n
        allCom = []
        self.dfs(left, right, allCom, '')
        return allCom
    def dfs(self, left, right, allCom, com):     
        if left < 0 or right < 0 or left > right:
            return 
        if left == 0 and right == 0:
            allCom.append(com)
        self.dfs(left - 1, right, allCom, com + '(')
        self.dfs(left, right - 1, allCom, com + ')')
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - DFS (2)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(0, 0, 0, "", n, res)
        return  res
    
    def dfs(self, index, l_cnt, r_cnt, tmp_s, n, res):
        if index == 2 * n:
            res.append(tmp_s)
        
        if index > 2 * n:
            return 
        
        # add left
        if l_cnt < n:
            self.dfs(index + 1, l_cnt + 1, r_cnt, tmp_s + '(', n, res)
            
        # add right (right should always less than the left)
        if r_cnt < n and r_cnt < l_cnt:
            self.dfs(index + 1, l_cnt, r_cnt + 1, tmp_s + ')', n, res)
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
