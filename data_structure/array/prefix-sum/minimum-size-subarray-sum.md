# Minimum Size Subarray Sum 406 \(M\)

## Problem

Given an array of `n` positive integers and a positive integer `s`, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return -1 instead.Example

**Example 1:**

```text
Input: [2,3,1,2,4,3], s = 7
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

**Example 2:**

```text
Input: [1, 2, 3, 4, 5], s = 100
Output: -1
```

Challenge

If you have figured out the O\(nlog n\) solution, try coding another solution of which the time complexity is O\(n\).

## Solution - Prefix Sum

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        ans = float('inf')
        for start in range(len(nums)):
            sum_val = 0
            for end in range(start, len(nums)):
                sum_val+=nums[end]
                if sum_val >= s:
                    ans = min(ans, end - start + 1)
        return ans if ans != float('inf') else -1
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^2\)**
* **Space Complexity: O\(1\)**

## Solution - Prefix Sum \(2\)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        if not nums:
            return -1
        prefix_sum = self.get_prefix_sum(nums)
        
        min_length = float('inf')
        for start in range(len(nums)):
            for end in range(start, len(nums)):
                # WARNING!
                # should be end + 1
                if prefix_sum[end + 1] - prefix_sum[start] >= s:
                    min_length = min(min_length, end - start + 1)
        return min_length if min_length != float('inf') else -1
    
    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^2\)**
* **Space Complexity: O\(n\)**

## Solution - Prefix Sum + Binary Search

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        if not nums:
            return -1
        prefix_sum = self.get_prefix_sum(nums)
        min_length = float('inf')
        for start in range(len(nums)):
            # here the start, end indexes for binary search
            # are based on the original nums list 
            # so the end index should be len(prefix_sum) - 2 
            end = self.get_end_of_subarray(prefix_sum, start, len(prefix_sum) - 2, s)
            # WARNING!
            # since it might not found 
            if end:
                min_length = min(min_length, end - start + 1)
        return min_length if min_length != float('inf') else -1

    def get_end_of_subarray(self, prefix_sum, start, end, s):
        left, right = start, end
        while left + 1 < right:
            mid = (left + right)//2
            if prefix_sum[mid + 1] - prefix_sum[start] >= s:
                right = mid
            else:
                left = mid
        # want to find the most left ones 
        if prefix_sum[left + 1] - prefix_sum[start] >= s:
            return left
        if prefix_sum[right + 1] - prefix_sum[start] >= s:
            return right
        return None
        
    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(nlogn\)**
* **Space Complexity: O\(n\)**

## Solution - Two Pointers

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        if not nums:
            return -1
        
        n = len(nums)
        min_length = float('inf')
        sum_of_subarray = 0
        j = 0
        for i in range(len(nums)):
            while j < n and sum_of_subarray < s:
                sum_of_subarray+=nums[j]
                j+=1
            if sum_of_subarray >= s:
                # j + 1 already previously 
                min_length = min(min_length, j - i)
            sum_of_subarray-=nums[i]
        return min_length if min_length != float('inf') else -1

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(1\)**

