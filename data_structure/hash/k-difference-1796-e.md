# K-Difference 1796 \(E\)

## Problem

In this challenge, you will be given an array of integers, each unique within the array, and an integer representing a target difference. Determine the number of pairs of elements in the array that have a difference equal to the target difference.  
For example, consider the array \[1, 3, 5\] and a target difference 2. There are two pairs:\[1, 3\] and \[3, 5\],that have the target difference.you must return an integer count of the number of pairs within a having a difference of k.

* 5 &lt;= n &lt;= 10^5.
* Each element of a,a\[i\] &lt;= 2 \* 10^9.
* Each a\[i\] is unique within a.
* 1 &lt;= target &lt;= 10^9.

Example

Example 1:

```text
Input: nums = [1, 3, 5, 7], target = 2
Output: 3
Explanation:
3 - 1 = 2
5 - 3 = 2
7 - 5 = 2
```

Example 2:

```text
Input: nums = [7, 2, 6], target = 2 
Output: 0
Explanation:
no pair have a difference of k 
```

Tags

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: a integer array
    @param target: 
    @return: return a integer
    """
    def KDifference(self, nums, target):
        # write your code here
        cnt = 0
        s = set()
        
        for n in nums:
            if (n - target) in s:
                cnt+=1
            if (n + target) in s:
                cnt+=1
            
            s.add(n)
        return cnt
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

