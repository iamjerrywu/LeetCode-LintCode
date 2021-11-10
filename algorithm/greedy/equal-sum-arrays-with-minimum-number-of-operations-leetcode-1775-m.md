# Equal Sum Arrays With Minimum Number of Operations (LeetCode 1775) (M)

## Problem

You are given two arrays of integers `nums1` and `nums2`, possibly of different lengths. The values in the arrays are between `1` and `6`, inclusive.

In one operation, you can change any integer's value in **any **of the arrays to **any** value between `1` and `6`, inclusive.

Return _the minimum number of operations required to make the sum of values in _`nums1`_ equal to the sum of values in _`nums2`_._ Return `-1`​​​​​ if it is not possible to make the sum of the two arrays equal.

**Example 1:**

```
Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
```

**Example 2:**

```
Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
```

**Example 3:**

```
Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. 
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].
```

**Constraints:**

* `1 <= nums1.length, nums2.length <= 105`
* `1 <= nums1[i], nums2[i] <= 6`

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        total_1 = sum(nums1)
        total_2 = sum(nums2)
        if total_1 == total_2:
            return 0
    
        if total_1 > total_2:
            diff_list = [num - 1 for num in nums1] + [6 - num for num in nums2]
        else:
            diff_list = [6 - num for num in nums1] + [num - 1 for num in nums2]
        
        diff_list.sort(reverse = True)
        
        diff = abs(total_1 - total_2)
        
        cnt = 0
        for i in range(len(diff_list)):
            diff-=diff_list[i]
            cnt+=1
            if diff <= 0:
                return cnt
            
        return -1
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(nlogn)**
* **Space Complexity: O(n)**
