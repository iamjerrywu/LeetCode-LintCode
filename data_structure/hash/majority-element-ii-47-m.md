# Majority Element II 47 \(M\)

## Problem

Given an integer array of size `n`, find all elements that appear more than `⌊ n/3 ⌋` times.

**Follow-up:** Could you solve the problem in linear time and in O\(1\) space?

**Example 1:**

```text
Input: nums = [3,2,3]
Output: [3]
```

**Example 2:**

```text
Input: nums = [1]
Output: [1]
```

**Example 3:**

```text
Input: nums = [1,2]
Output: [1,2]
```

**Constraints:**

* `1 <= nums.length <= 5 * 104`
* `-109 <= nums[i] <= 109`

## Solution - Hash Map

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ref = len(nums)//3
        cnt = {}
        
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        ans = []
        for k, v in cnt.items():
            if v > ref:
                ans.append(k)
        ans.sort()
        return ans
        
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

