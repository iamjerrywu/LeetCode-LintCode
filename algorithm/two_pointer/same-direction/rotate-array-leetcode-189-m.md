# Rotate Array (LeetCode 189) (M)

## Problem

Given an array, rotate the array to the right by `k` steps, where `k` is non-negative.

&#x20;

**Example 1:**

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 105`
* `-231 <= nums[i] <= 231 - 1`
* `0 <= k <= 105`

&#x20;

**Follow up:**

* Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.
* Could you do it in-place with `O(1)` extra space?



## Solution - Using Extra Space

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%=n
        new_nums = [0] * n
        
        # approach 1
        new_nums = nums[n - k:] + nums[0 : n - k]
        
        # approach 2
        # for i in range(len(nums)):
        #     new_nums[(i + k)%n] = nums[i]
        
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]
        return nums
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



## Solution - Two Pointer

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%=n
        nums.reverse()
        
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        return 
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
* **Space Complexity: O(1)**

