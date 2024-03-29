# Two Sum VII 1879 (H)

## Problem

Given an array of integers that is already **sorted in ascending absolute order**, find two numbers so that the sum of them equals a specific number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Note: the subscript of the array starts with 0

You are not allowed to sort this array.

* It is guaranteed that all numbers in the numsnums is distinct.
* The length of numsnums is \leq 100\\,000≤100000.
* The number in numsnums is \leq 10^9≤109.

Example

```
Input: [0,-1,2,-3,4]1Output: [[1,2],[3,4]]Explanation: nums[1] + nums[2] = -1 + 2 = 1, nums[3] + nums[4] = -3 + 4 = 1You can return [[3,4],[1,2]], the system will automatically help you sort it to [[1,2],[3,4]]. But [[2,1],[3,4]] is invaild.
```

Challenge

\mathcal{O}(n)O(n) time complexity and \mathcal{O}(1)O(1) extra space

## Solution&#x20;

Since the numbers is in absolute sorted order (i.e: -1, 2, 3, -4, 8, 9, -10)

First find out left (min), right(max), then use opposite two pointer solution

* nums\[left] + nums\[right] < target: move left
* nums\[left] + nums\[right] > target: move right
* nums\[left] + nums\[right] == target, append to ans

Note:

when move left, should find the next bigger left

* if nums\[left] < 0
  * First i from left - 1 to 0, if nums\[i] < 0, return i
  * Second, (if first don't return, means next left > 0), i from 0 to n - 1, if nums\[i] >= 0, then return i
* If nums\[left] > 0
  * i from left + 1 to n - 1, if nums\[i] >= 0, then return i

If all no, then return -1

Same approach using for finding next right (next smaller right)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
    """
    def twoSumVII(self, nums, target):
        # write your code here

        n = len(nums)
        if n == 0:
            return []
        
        left = 0
        right = 0
        # find the min(left), max(right)
        for i in range(n):
            if nums[i] > nums[right]:
                right = i
            if nums[i] < nums[left]:
                left = i
        ans = []
        while nums[left] < nums[right]:
            if nums[left] + nums[right] < target:
                left = self.next_left(left, nums)
                if left == -1:
                    break
            elif nums[left] + nums[right] > target:
                right = self.next_right(right, nums)
                if right == -1:
                    break
            else:
                tmp = [left, right]
                if left > right:
                    tmp[0], tmp[1] = tmp[1], tmp[0]
                ans.append(tmp)
                left = self.next_left(left, nums)
                if left == -1:
                    break
        return ans
    
    def next_left(self, left, nums):
        n = len(nums)
        if nums[left] < 0:
            for i in range(left - 1, -1, -1):
                if nums[i] < 0:
                    return i
            for i in range(n):
                if nums[i] >= 0:
                    return i
            return -1
        for i in range(left + 1, n):
            if nums[i] >= 0:
                return i
        return -1
    
    def next_right(self, right, nums):
        n = len(nums)
        if nums[right] > 0:
            for i in range(right - 1, -1, -1):
                if nums[i] > 0:
                    return i
            for i in range(n):
                if nums[i] <= 0:
                    return i
            return -1
        for i in range(right + 1, n):
            if nums[i] <= 0:
                return i
        return -1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**



## Solution - Binary Search

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
    """
    def twoSumVII(self, nums, target):
        # write your code here
        ans = []
        for i in range(len(nums)):
            prev = target - nums[i]
            if abs(nums[0]) <= abs(prev) and abs(prev) <= abs(nums[i - 1]):
                idx = self.binary_search(nums, 0, i, abs(prev))
                if idx != -1:
                    if prev == nums[idx]:
                        ans.append((idx, i))
                    # consider target may be +/- exist in list at the same time
                    # since already find the first one, then 'first + 1' might also be the target
                    if idx < (i - 1) and prev == nums[idx + 1]:
                        ans.append((idx + 1, i))
        return ans        
    
    def binary_search(self, nums, start, end, target):
        while start + 1 < end:
            mid = (start + end)//2
            if abs(nums[mid]) < target:
                start = mid
            elif abs(nums[mid]) > target:
                end = mid
            # trying to find the first one
            else:
                end = mid
        if abs(nums[start]) == target:
            return start
        elif abs(nums[end]) == target:
            return end
        return -1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn)**
* **Space Complexity: O(1)**
