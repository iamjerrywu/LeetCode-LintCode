# The kth Factor of n (LeetCode 1492) (M)

## Problem

Given two positive integers `n` and `k`.

A factor of an integer `n` is defined as an integer `i` where `n % i == 0`.

Consider a list of all factors of `n` sorted in **ascending order**, return _the_ `kth` _factor_ in this list or return **-1** if `n` has less than `k` factors.

&#x20;

**Example 1:**

```
Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
```

**Example 2:**

```
Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
```

**Example 3:**

```
Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
```

**Example 4:**

```
Input: n = 1, k = 1
Output: 1
Explanation: Factors list is [1], the 1st factor is 1.
```

**Example 5:**

```
Input: n = 1000, k = 3
Output: 4
Explanation: Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000].
```

&#x20;

**Constraints:**

* `1 <= k <= n <= 1000`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cnt = 1
        for num in range(1, n + 1):
            if n%num == 0:
                if cnt == k:
                    return num
                cnt+=1
        return -1
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**

****

## Solution&#x20;

![](<../../.gitbook/assets/Screen Shot 2021-11-22 at 12.46.11 PM.png>)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cnt = 1
        divisors = []
        sqrt_n = int(sqrt(n))
        for num in range(1, sqrt_n + 1):
            if n%num == 0:
                if cnt == k:
                    return num
                cnt+=1
                divisors.append(num)
        # if duplicated, need to skip it
        if sqrt_n * sqrt_n == n:
            k+=1
        n_div = len(divisors)
        return n // divisors[-(k - n_div)] if k <= 2 * n_div else -1
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(sqrt(n))**
* **Space Complexity: O(1)**

****
