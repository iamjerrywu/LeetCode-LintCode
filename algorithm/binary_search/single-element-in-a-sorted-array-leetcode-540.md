# Single Element in a Sorted Array (LeetCode 540)

## Problem

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return _the single element that appears only once_.

Your solution must run in `O(log n)` time and `O(1)` space.

&#x20;

**Example 1:**

```
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
```

**Example 2:**

```
Input: nums = [3,3,7,7,10,11,11]
Output: 10
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 105`
* `0 <= nums[i] <= 105`

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return self.binary_search(nums)

    def binary_search(self, nums):
        start, end = 0, len(nums) - 1
        n = len(nums)
        
        while start + 1 < end:
            mid = start + (end - start)//2
            
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            
            if nums[mid] == nums[mid + 1] and (n - (mid + 2))%2 == 1:
                start = mid + 2
            if nums[mid] == nums[mid + 1] and (n - (mid + 2))%2 == 0:
                end = mid - 1
            if nums[mid] == nums[mid - 1] and (mid - 1)%2 == 1:
                end = mid - 2
            if nums[mid] == nums[mid - 1] and (mid - 1)%2 == 0:
                start = mid + 1
        
        return nums[start]
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

* **Time Complexity: O(logn)**
* **Space Complexity: O(1)**
