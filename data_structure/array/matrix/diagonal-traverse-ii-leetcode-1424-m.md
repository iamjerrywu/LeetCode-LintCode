# Diagonal Traverse II (LeetCode 1424) (M)

## Problem

****

Given a 2D integer array `nums`, return _all elements of_ `nums` _in diagonal order as shown in the below images_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/04/08/sample\_1\_1784.png)

```
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/04/08/sample\_2\_1784.png)

```
Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 105`
* `1 <= nums[i].length <= 105`
* `1 <= sum(nums[i].length) <= 105`
* `1 <= nums[i][j] <= 105`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        # find max length of row
        n = 0
        for row in nums:
            n = max(n, len(row))
        m = len(nums)
        
        
        rec = [[] for _ in range(m + n - 1)]
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                rec[i + j].append([i, nums[i][j]])
        
        ans = []
        for arr in rec:
            arr.sort(key = lambda a:(-a[0]))
            for ele in arr:
                ans.append(ele[1])
    
        return ans
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

* **Time Complexity:**
* **Space Complexity:**

****
