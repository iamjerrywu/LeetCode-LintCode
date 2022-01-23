# Remove Invalid Parentheses 780 (H)

## Problem

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

The input string may contain letters other than the parentheses `(` and `)`.Example

**Example 1:**

```
Input:"()())()"Ouput:["(())()","()()()"]
```

**Example 2:**

```
Input:"(a)())()"Output: ["(a)()()", "(a())()"]
```

**Example 3:**

```
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

{% tab title="Python (Better)" %}
```python
import collections
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        queue = collections.deque([s])
        find = False
        seen = set([s])
        while queue:
            for _ in range(len(queue)):
                cur_s = queue.popleft()

                if self.is_valid(cur_s):
                    ans.append(cur_s)
                    find = True
                if not find:
                    for i in range(len(cur_s)):
                        if cur_s[i].isalpha():
                            continue
                        new_s = cur_s[:i] + cur_s[i + 1:]
                        if new_s not in seen:
                            seen.add(new_s)
                            queue.append(new_s)
            if find:
                break
        return ans
    
    def is_valid(self, s):
        cnt = 0
        for c in s:
            if cnt < 0:
                return False
            if c == '(':
                cnt+=1
            if c == ')':
                cnt-=1
        return cnt == 0
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(2^n \* n)**
* **Space Complexity: O(n)**
