# Find Pivot Index (1068) (E)

## Problem

Given an array of integers `nums`, calculate the **pivot index** of this array.

The **pivot index** is the index where the sum of all the numbers **strictly** to the left of the index is equal to the sum of all the numbers **strictly** to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return _the **leftmost pivot index**_. If no such index exists, return -1.

**Example 1:**

```
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
```

**Example 2:**

```
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
```

**Example 3:**

```
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
```

**Constraints:**

* `1 <= nums.length <= 104`
* `-1000 <= nums[i] <= 1000`

## Solution - Prefix Sums

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sums = self.build_prefix_sums(nums)
        for i in range(len(nums)):
            if prefix_sums[i] == prefix_sums[len(nums)] - prefix_sums[i + 1]:
                return i
        return -1
    def build_prefix_sums(self, nums):
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
        return prefix_sums
        
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**



## Solution - Enumeration

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        
        for i in range(len(nums)):
            right_sum-=nums[i]
            if left_sum == right_sum:
                return i
            left_sum+=nums[i]
        return -1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**
