# Maximum Value after Insertion (LeetCode 1881) (M)

## Problem

You are given a very large integer `n`, represented as a string,​​​​​​ and an integer digit `x`. The digits in `n` and the digit `x` are in the **inclusive** range `[1, 9]`, and `n` may represent a **negative** number.

You want to **maximize** `n`**'s numerical value** by inserting `x` anywhere in the decimal representation of `n`​​​​​​. You **cannot** insert `x` to the left of the negative sign.

* For example, if `n = 73` and `x = 6`, it would be best to insert it between `7` and `3`, making `n = 763`.
* If `n = -55` and `x = 2`, it would be best to insert it before the first `5`, making `n = -255`.

Return _a string representing the **maximum** value of_ `n`_​​​​​​ after the insertion_.

**Example 1:**

```
Input: n = "99", x = 9
Output: "999"
Explanation: The result is the same regardless of where you insert 9.
```

**Example 2:**

```
Input: n = "-13", x = 2
Output: "-123"
Explanation: You can make n one of {-213, -123, -132}, and the largest of those three is -123.
```

**Constraints:**

* `1 <= n.length <= 105`
* `1 <= x <= 9`
* The digits in `n`​​​ are in the range `[1, 9]`.
* `n` is a valid representation of an integer.
* In the case of a negative `n`,​​​​​​ it will begin with `'-'`.

## Solution&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        val = 0
        l = len(n)
        if int(n) > 0:
            i = 0
            while i < l and int(n[i]) >= x:
                i+=1
            if n[:i]:
                val+= int(n[:i]) * (10**(l - i + 1))
            if n[i:]:
                val+=int(n[i:])
            val+= x * (10**(l - i))
            return str(val)
        else:
            i = 1
            while i < l and int(n[i]) <= x:
                i+=1
            if n[1:i]:
                val+= int(n[1:i]) * (10**(l - i + 1))
            if n[i:]:
                val+=int(n[i:])
            val+= x * (10**(l - i)) 
            return str(-val)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
