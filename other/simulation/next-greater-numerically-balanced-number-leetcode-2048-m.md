# Next Greater Numerically Balanced Number (LeetCode 2048) (M)



## Problem



An integer `x` is **numerically balanced** if for every digit `d` in the number `x`, there are **exactly** `d` occurrences of that digit in `x`.

Given an integer `n`, return _the **smallest numerically balanced** number **strictly greater** than _`n`_._

&#x20;

**Example 1:**

```
Input: n = 1
Output: 22
Explanation: 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
```

**Example 2:**

```
Input: n = 1000
Output: 1333
Explanation: 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
```

**Example 3:**

```
Input: n = 3000
Output: 3133
Explanation: 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.
```

&#x20;

**Constraints:**

* `0 <= n <= 106`

&#x20;

## Solution

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # since should strictly greater
        n = n + 1
        while True:
            if self.is_beautiful(n):
                return n
            n+=1
    
    def is_beautiful(self, n):
        cnt = collections.defaultdict(int)
        while n:
            digit = n%10
            if digit == 0:
                return False
            cnt[digit]+=1
            n//=10
        for k, v in cnt.items():
            if k != v:
                return False
        return True
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: **
* **Space Complexity:**
