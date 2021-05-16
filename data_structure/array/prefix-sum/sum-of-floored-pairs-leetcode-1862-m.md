# Sum of Floored Pairs \(LeetCode 1862\) \(M\)

## Problem

Given an integer array `nums`, return the sum of `floor(nums[i] / nums[j])` for all pairs of indices `0 <= i, j < nums.length` in the array. Since the answer may be too large, return it **modulo** `109 + 7`.

The `floor()` function returns the integer part of the division.

**Example 1:**

```text
Input: nums = [2,5,9]
Output: 10
Explanation:
floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
floor(5 / 2) = 2
floor(9 / 2) = 4
floor(9 / 5) = 1
We calculate the floor of the division for every pair of indices in the array then sum them up.
```

**Example 2:**

```text
Input: nums = [7,7,7,7,7,7,7]
Output: 49
```

**Constraints:**

* `1 <= nums.length <= 105`
* `1 <= nums[i] <= 105`

## Solution - Brute Force

{% hint style="danger" %}
Would LTE
{% endhint %}

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        record = {}
        for num1 in nums:
            for num2 in nums:
                reco rd[floor(num1/num2)] = record.get(floor(num1/num2), 0) + 1
        return sum([k * v for k, v in record.items()])
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^2\)**
* **Space Complexity: O\(n\)**

