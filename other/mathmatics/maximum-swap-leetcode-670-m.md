# Maximum Swap (LeetCode 670) (M)

## Problem

You are given an integer `num`. You can swap two digits at most once to get the maximum valued number.

Return _the maximum valued number you can get_.

&#x20;

**Example 1:**

```
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
```

**Example 2:**

```
Input: num = 9973
Output: 9973
Explanation: No swap.
```

&#x20;

**Constraints:**

* `0 <= num <= 108`

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = [int(c) for c in str(num)]
        last_index = {}
        
        for i, val in enumerate(num_list):
            last_index[val] = i
        for i in range(len(num_list)):
            for val in range(9, num_list[i], -1):
                if val in last_index and last_index[val] > i:
                    num_list[i], num_list[last_index[val]] = num_list[last_index[val]], num_list[i]
                    
                    return int("".join([str(val) for val in num_list]))
        return num
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

* **Time Complexity: O(n \* 10)**
* **Space Complexity: O(n)**

