# Find the Duplicate Number 633 (H)

## Problem

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return _this repeated number_.

You must solve the problem **without** modifying the array `nums` and uses only constant extra space.

**Example 1:**

```
Input: nums = [1,3,4,2,2]
Output: 2
```

**Example 2:**

```
Input: nums = [3,1,3,4,2]
Output: 3
```

**Example 3:**

```
Input: nums = [1,1]
Output: 1
```

**Example 4:**

```
Input: nums = [1,1,2]
Output: 1
```

**Constraints:**

* `1 <= n <= 105`
* `nums.length == n + 1`
* `1 <= nums[i] <= n`
* All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.

**Follow up:**

* How can we prove that at least one duplicate number must exist in `nums`?
* Can you solve the problem in linear runtime complexity?

## Solution - Sort

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        # write your code here
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn)**
* **Space Complexity: O(n)**
  * Python timsort() as default sorting algorithm
    * When doing merge, would use extra O(n) space&#x20;



## Solution - HashSet

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        # write your code here
        ref = set()
        for num in nums:
            if num in ref:
                return num
            else:
                ref.add(num)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**



## Solution - Binary Search

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        # write your code here
        left, right = 1, len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left)//2
            if self.count(nums, mid) <= mid:
                left = mid
            else:
                right = mid
        # because that number might appeared multiple times, should <= left
        if self.count(nums, left) <= left:
            return right
        return left
    
    # count how many number <= mid
    def count(self, nums, mid):
        cnt = 0
        for num in nums:
            if num <= mid:
                cnt+=1
        return cnt

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nlogn)**
* **Space Complexity: O(1)**



## Solution - Two Pointers

![](<../../.gitbook/assets/Screen Shot 2021-06-05 at 7.28.05 PM.png>)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow = nums[0]
        print(slow, fast)
        while True:
            
            if slow == fast:
                return slow
            slow = nums[slow]
            fast = nums[fast]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**
