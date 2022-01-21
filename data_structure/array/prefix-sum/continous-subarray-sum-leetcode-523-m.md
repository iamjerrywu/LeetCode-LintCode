# Continous Subarray Sum (LeetCode 523) (M)

## Problem

Given an integer array `nums` and an integer `k`, return `true` _if_ `nums` _has a continuous subarray of size **at least two** whose elements sum up to a multiple of_ `k`_, or_ `false` _otherwise_.

An integer `x` is a multiple of `k` if there exists an integer `n` such that `x = n * k`. `0` is **always** a multiple of `k`.

&#x20;

**Example 1:**

```
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
```

**Example 2:**

```
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
```

**Example 3:**

```
Input: nums = [23,2,6,4,7], k = 13
Output: false
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 105`
* `0 <= nums[i] <= 109`
* `0 <= sum(nums[i]) <= 231 - 1`
* `1 <= k <= 231 - 1`

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # prefix_sum - cur_sum)%k == 0
        # prefix_sum%k == cur_sum%k
        
        # storing the prefix sum index (the earliest one)
        # prefix_sum = 0 need to be considered here, and set index to -1
        rec = {0:-1} 
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            if prefix_sum%k in rec:
                if i - rec[prefix_sum%k] >= 2:
                    return True
            # only store the earlist one index
            else:
                rec[prefix_sum%k] = i
        return False
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

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**

****
