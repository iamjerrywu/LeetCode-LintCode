# Expression Add Operators (LeetCode 282) (H)

## Problem

****

Given a string `num` that contains only digits and an integer `target`, return _**all possibilities** to insert the binary operators_ `'+'`_,_ `'-'`_, and/or_ `'*'` _between the digits of_ `num` _so that the resultant expression evaluates to the_ `target` _value_.

Note that operands in the returned expressions **should not** contain leading zeros.

&#x20;

**Example 1:**

```
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
```

**Example 2:**

```
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
```

**Example 3:**

```
Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
```

&#x20;

**Constraints:**

* `1 <= num.length <= 10`
* `num` consists of only digits.
* `-231 <= target <= 231 - 1`



## Solution&#x20;

Prev: Store the previous calculated value

cur: store the current calculated (accumulated) value

val: the latest integer we traversed

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []

        self.dfs(0, num, 0, 0, 0, "", ans, target)
        return ans
    
    def dfs(self, index, num, prev, cur, val, s, ans, tar):
        if index == len(num):
            if cur == tar:
                ans.append(s)
            return
        
        for i in range(index, len(num)):
            # if leading zero, then skip
            if i > index and num[index] == '0':
                return 
            
            val = int(num[index:i + 1])
            
            if not s:
                self.dfs(i + 1, num, 0, val, val, str(val), ans, tar)
            else:
                # no need to deal with backtracking, since we use variable in stack
                self.dfs(i + 1, num, cur, cur + val, val, s + "+" + str(val), ans, tar)
                self.dfs(i + 1, num, cur, cur - val, val, s + "-" + str(val), ans, tar)
                self.dfs(i + 1, num, prev, prev + (cur - prev) * val, val, s + "*" + str(val), ans, tar)
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

****
