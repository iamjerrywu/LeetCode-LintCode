# Backpack V 563 \(M\)

## Problem

Given n items with size `nums[i]` which an integer array and all positive numbers. An integer `target` denotes the size of a backpack. Find the number of possible fill the backpack.

`Each item may only be used once`Example

Given candidate items `[1,2,3,3,7]` and target `7`,

```text
A solution set is: 
[7]
[1, 3, 3]
```

return `2`

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] +=dp[j - num]
        
        return dp[target]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

