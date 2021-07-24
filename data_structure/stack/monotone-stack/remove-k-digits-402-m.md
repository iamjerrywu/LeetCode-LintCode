# Remove K Digits 402 \(M\)

## Problem

Given string num representing a non-negative integer `num`, and an integer `k`, return _the smallest possible integer after removing_ `k` _digits from_ `num`.

**Example 1:**

```text
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
```

**Example 2:**

```text
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
```

**Example 3:**

```text
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
```

**Constraints:**

* `1 <= k <= num.length <= 105`
* `num` consists of only digits.
* `num` does not have any leading zeros except for the zero itself.

## Solution - Brute Force

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        for i in range(k):
            num = self.remove_digit(num)
        num = self.remove_zeros(num)
        return num
    
    def remove_digit(self, num):
        for i in range(1, len(num)):
            if num[i] < num[i - 1]:
                return num[:i - 1] + num[i:]
        # remove the last one
        return num[:-1]
    
    
    def remove_zeros(self, num):
        cnt = 0
        for i in range(len(num)):
            if num[i] == '0':
                cnt+=1
            else:
                break
        if cnt == len(num):
            return '0'
        else:
            return num[cnt:]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution 

{% tabs %}
{% tab title="Python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

