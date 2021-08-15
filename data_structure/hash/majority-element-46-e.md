# Majority Element 46 \(E\)

## Problem

Given an array `nums` of size `n`, return _the majority element_.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

```text
Input: nums = [3,2,3]
Output: 3
```

**Example 2:**

```text
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints:**

* `n == nums.length`
* `1 <= n <= 5 * 104`
* `-231 <= nums[i] <= 231 - 1`

## Solution - Hash Map

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = {}
        for num in nums:
            major_cnt = 0
            major_ele = 0
            cnt[num] = cnt.get(num, 0) + 1
        for k, v in cnt.items():
            if v > major_cnt:
                major_ele = k
                major_cnt = v
        return major_ele
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

