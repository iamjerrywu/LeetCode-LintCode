# Find Greatest Common Divisor of Array (LeetCode 5850) (E)

## Problem

Given an integer array `nums`, return _the **greatest common divisor** of the smallest number and largest number in_ `nums`.

The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.

**Example 1:**

```
Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
```

**Example 2:**

```
Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.
```

**Example 3:**

```
Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.
```

**Constraints:**

* `2 <= nums.length <= 1000`
* `1 <= nums[i] <= 1000`

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        
        for i in range(min_val, -1, -1):
            if min_val%i == 0 and max_val%i == 0:
                return i
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
