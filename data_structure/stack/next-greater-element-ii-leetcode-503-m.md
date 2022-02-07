# Next Greater Element II (LeetCode 503) (M)

## Problem



Given a circular integer array `nums` (i.e., the next element of `nums[nums.length - 1]` is `nums[0]`), return _the **next greater number** for every element in_ `nums`.

The **next greater number** of a number `x` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return `-1` for this number.

&#x20;

**Example 1:**

```
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
```

**Example 2:**

```
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 104`
* `-109 <= nums[i] <= 109`



## Solution - Stack Two Pass

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [float('-inf')] * len(nums)
        
        # round 1
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1]
            stack.append(nums[i])
        
        # round 2
        if stack:
            for i in range(len(nums) - 1, -1, -1):
                if not stack:
                    break
                while stack and stack[-1] <= nums[i]:
                    stack.pop()
                if ans[i] == float('-inf') and stack:
                    ans[i] = stack[-1]
        
        for i in range(len(ans)):
            if ans[i] == float('-inf'):
                ans[i] = -1
        return ans
        
```
{% endtab %}

{% tab title="Python (Better)" %}
```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        
        
        # first round
        # 5, 3, 2, 4
        # 5, (3, 2), 4  => here that both 3, 2 will be popped
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        
        # second loop, since we need to find if after wrapper
        # any val in the array is bigger than element in the stack
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
        return ans
        
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

****
