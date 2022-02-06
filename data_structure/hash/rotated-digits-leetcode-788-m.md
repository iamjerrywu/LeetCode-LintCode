# Rotated Digits (LeetCode 788) (M)

## Problem

An integer `x` is a **good** if after rotating each digit individually by 180 degrees, we get a valid number that is different from `x`. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

* `0`, `1`, and `8` rotate to themselves,
* `2` and `5` rotate to each other (in this case they are rotated in a different direction, in other words, `2` or `5` gets mirrored),
* `6` and `9` rotate to each other, and
* the rest of the numbers do not rotate to any other number and become invalid.

Given an integer `n`, return _the number of **good** integers in the range_ `[1, n]`.

&#x20;

**Example 1:**

```
Input: n = 10
Output: 4
Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
```

**Example 2:**

```
Input: n = 1
Output: 0
```

**Example 3:**

```
Input: n = 2
Output: 1
```

&#x20;

**Constraints:**

* `1 <= n <= 104`

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def rotatedDigits(self, n: int) -> int:
        mapping = {0: 0, 
                   1: 1, 
                   2: 5, 
                   3:-1,
                   4:-1,
                   5: 2,
                   6: 9,
                   7:-1,
                   8: 8,
                   9: 6}
        cnt = 0
        for num in range(1, n + 1):
            if self.rotate_valid(num, mapping):
                cnt+=1
        return cnt
    
    def rotate_valid(self, num, mapping):
        digits = [int(c) for c in str(num)]
        new_num = 0
        for d in digits:
            if mapping[d] < 0:
                return False
            new_num = new_num * 10 + mapping[d]
        return new_num != num
        
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

* **Time Complexity: O(nlogn)**
* **Space Complexity: O(1)**
