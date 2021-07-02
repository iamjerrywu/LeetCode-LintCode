# First Missing Positive 189 \(M\)

## Problem

Given an **unsorted** integer array, find the first **missing** positive integer.Example

**Example 1:**

```text
Input:[1,2,0]Output:3
```

**Example 2:**

```text
Input:[3,4,-1,1]Output:2
```

Challenge

Your algorithm should run in O\(_n_\) time and uses constant space.

## Solution - Hash Table

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
           ref = set() # O(n) space
           for num in nums: O(n)
                     ref.add(num)
           max_val = max(ref)
           if max_val <= 0:
                  return 1
           for i in range(1, max_val): O(n)
                 if i not in ref: # O(1)
                     return i
          return max_val + 1 
```

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(n\)**

## Solution - Greedy

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # first scan: put the right number in the right index
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # second scan: check missing number by index, if not match, then that's answer 
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
```

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(1\)**

