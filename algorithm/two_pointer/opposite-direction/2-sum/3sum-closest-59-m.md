# 3Sum Closest 59 (M)

## Problem

Given an array `S` of `n` integers, find three integers in `S` such that the sum is closest to a given number, `target`. Return the sum of the three integers.

You may assume that each input would have exactly one solution.Example

**Example 1:**

Input:

```
numbers = [2,7,11,15]
target = 3
```

Output:

```
20
```

Explanation:

2+7+11=20\
**Example 2:**

Input:

```
numbers = [-1,2,1,-4]
target = 1
```

Output:

```
2
```

Explanation:

\-1+2+1=2Challenge

O(n^2)O(n​2​​) time, O(1)O(1) extra space

## Solution&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        if not numbers:
            return 0
        
        numbers.sort()
        min_diff = float('inf')
        
        for i in range(0, len(numbers) - 2):
            base = numbers[i]
            left, right = i + 1, len(numbers) - 1
            while left < right:
                l_r_sum = numbers[left] + numbers[right]
                if min_diff > abs(target - base - l_r_sum):
                    ans = l_r_sum + base
                    min_diff = abs(target - base - l_r_sum)
                if l_r_sum + base > target:
                    right-=1
                elif l_r_sum + base < target:
                    left+=1
                else:
                    return ans
        return ans
```
{% endtab %}

{% tab title="Python (Better)" %}
```python
 class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums)):
            base = nums[i]
            
            tar = target - base
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum_val = base + nums[l] + nums[r]
                if nums[l] + nums[r] > tar:
                    r-=1
                elif nums[l] + nums[r] < tar:
                    l+=1
                else:
                    return base + nums[l] + nums[r]
                
                if abs(sum_val - target) < min_diff:
                    min_diff = abs(sum_val - target)
                    ans = sum_val
                    
        return ans
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n^2)**
  * Sort: O(nlogn)
  * Two loops:
    * O(n^2)
* **Space Complexity: O(1)**
