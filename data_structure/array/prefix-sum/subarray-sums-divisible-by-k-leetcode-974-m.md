# Subarray Sums Divisible by K (LeetCode 974) (M)

## Problem



Given an integer array `nums` and an integer `k`, return _the number of non-empty **subarrays** that have a sum divisible by_ `k`.

A **subarray** is a **contiguous** part of an array.

&#x20;

**Example 1:**

```
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
```

**Example 2:**

```
Input: nums = [5], k = 9
Output: 0
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 3 * 104`
* `-104 <= nums[i] <= 104`
* `2 <= k <= 104`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_info = {0:1}
        sum_val = ans = 0
        for num in nums:
            sum_val+=num
            if sum_val%k in prefix_info:
                ans+=prefix_info[sum_val%k]
                prefix_info[sum_val%k]+=1
            else:
                prefix_info[sum_val%k] = 1
        return ans
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**

****
