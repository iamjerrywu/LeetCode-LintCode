# Array With Elements Not Equal to Average of Neighbors (LeetCode 1968) (M)

## Problem&#x20;

You are given a **0-indexed** array `nums` of **distinct** integers. You want to rearrange the elements in the array such that every element in the rearranged array is **not** equal to the **average** of its neighbors.

More formally, the rearranged array should have the property such that for every `i` in the range `1 <= i < nums.length - 1`, `(nums[i-1] + nums[i+1]) / 2` is **not** equal to `nums[i]`.

Return _**any** rearrangement of _`nums`_ that meets the requirements_.

**Example 1:**

```
Input: nums = [1,2,3,4,5]
Output: [1,2,4,5,3]
Explanation:
When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.
```

**Example 2:**

```
Input: nums = [6,2,0,9,7]
Output: [9,7,6,2,0]
Explanation:
When i=1, nums[i] = 7, and the average of its neighbors is (9+6) / 2 = 7.5.
When i=2, nums[i] = 6, and the average of its neighbors is (7+2) / 2 = 4.5.
When i=3, nums[i] = 2, and the average of its neighbors is (6+0) / 2 = 3.
```

**Constraints:**

* `3 <= nums.length <= 105`
* `0 <= nums[i] <= 105`

{% hint style="warning" %}
Problem really similar to [Prob.508 Wiggle Sort](wiggle-sort-508-m.md)
{% endhint %}

## Solution - Not In Place

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # because the num in nums is distinct
        # which means can sort first, 
        nums.sort()
        
        left, right = 0, len(nums) - 1
        ans = []
        while left <= right:
            if left <= right:
                ans.append(nums[left])
                left+=1
            if left <= right:
                ans.append(nums[right])
                right-=1
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

****

## Solution - In Place

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # because the num in nums is distinct
        # which means can sort first, 
        nums.sort()
        
        for i in range(1, len(nums), 2):
            if i + 1 < len(nums):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
