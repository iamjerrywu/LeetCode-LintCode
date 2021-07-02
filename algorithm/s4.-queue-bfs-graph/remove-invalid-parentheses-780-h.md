# Remove Invalid Parentheses 780 \(H\)

## Problem

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

The input string may contain letters other than the parentheses `(` and `)`.Example

**Example 1:**

```text
Input:"()())()"Ouput:["(())()","()()()"]
```

**Example 2:**

```text
Input:"(a)())()"Output: ["(a)()()", "(a())()"]
```

**Example 3:**

```text
Input:")(" Output: [""]
```

## Solution - BFS

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        res = []
        if not s:
            res.append('')
            return res
        
        queue = collections.deque([s])
        visited = set()
        visited.add(s)
        find = False

        while queue:
            cur_str = queue.popleft()
            if self.is_valid(cur_str):
                res.append(cur_str)
                find = True
            if find:
                continue            
            for i in range(len(cur_str)):
                if cur_str[i] != '(' and cur_str[i] != ')':
                    continue
                new_str = cur_str[0:i] + cur_str[i + 1:]
                if new_str not in visited:
                    visited.add(new_str)
                    queue.append(new_str)
        return res
    
    def is_valid(self, str):
        if not str:
            return True
        cnt = 0
        for c in str:
            if c == '(':
                cnt+=1
            if c == ')':
                cnt-=1
            if cnt < 0:
                return False
        if cnt == 0:
            return True
        return False
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

