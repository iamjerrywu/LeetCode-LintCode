# Degree of an Array (LeetCode 697) (E)

## Problem

Given a non-empty array of non-negative integers `nums`, the **degree** of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of `nums`, that has the same degree as `nums`.

&#x20;

**Example 1:**

```
Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
```

**Example 2:**

```
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
```

&#x20;

**Constraints:**

* `nums.length` will be between 1 and 50,000.
* `nums[i]` will be an integer between 0 and 49,999.

## Solution - Hash

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        rec = {} # left, right, cnt
        
        for i in range(len(nums)):
            if nums[i] not in rec:
                rec[nums[i]] = [i, i, 1]
            else:
                rec[nums[i]][1] = i
                rec[nums[i]][2]+=1
        ans = float('inf')
        max_cnt = float('-inf')
        for l, r, cnt in rec.values():
            if cnt > max_cnt:
                max_cnt = cnt
                ans = r - l + 1
            elif cnt == max_cnt:
                ans = min(ans, r - l + 1)
        return ans
        
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
