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
