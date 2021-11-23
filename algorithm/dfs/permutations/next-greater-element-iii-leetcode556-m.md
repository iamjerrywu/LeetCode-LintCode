# Next Greater Element III (LeetCode556) (M)



## Problem



Given a positive integer `n`, find _the smallest integer which has exactly the same digits existing in the integer_ `n` _and is greater in value than_ `n`. If no such positive integer exists, return `-1`.

**Note** that the returned integer should fit in **32-bit integer**, if there is a valid answer but it does not fit in **32-bit integer**, return `-1`.

&#x20;

**Example 1:**

```
Input: n = 12
Output: 21
```

**Example 2:**

```
Input: n = 21
Output: -1
```

&#x20;

**Constraints:**

* `1 <= n <= 231 - 1`



## Solution&#x20;

{% hint style="warning" %}
This problem is actually different from LeetCode 52: Next Permutation problem. Really similar, but in permutation, it would actually wrap, but in this problem we only need to find the larger one, so no wrap condition will happen.&#x20;
{% endhint %}

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = []
        tmp = n
        while tmp:
            digits.append(tmp%10)
            tmp//=10
        digits.reverse()
        
        ptr = len(digits) - 2
        while ptr >= 0 and digits[ptr] >= digits[ptr + 1]:
            ptr-=1
        print(ptr)
        if ptr < 0:
            return -1
        tar = ptr
        ptr = len(digits) - 1
        while ptr >= 0 and digits[ptr] <= digits[tar]:
            ptr-=1
        digits[ptr], digits[tar] = digits[tar], digits[ptr]
        
        # sort the numbers after tar
        digits[tar + 1:] = reversed(digits[tar + 1:])
        
        ans = 0
        pwr = len(digits) - 1
        for i in range(len(digits)):
            ans+=digits[i] * (10 ** pwr)
            pwr-=1
        
        return ans if ans <= (2**31 - 1) else -1
        
        
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
