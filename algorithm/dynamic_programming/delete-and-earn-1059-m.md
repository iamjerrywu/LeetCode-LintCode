# Delete and Earn 1059 \(M\)

## Problem

Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums\[i\] and delete it to earn nums\[i\] points. After, you must delete every element equal to nums\[i\] - 1 or nums\[i\] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

The length of nums is at most 20000.  
Each element nums\[i\] is an integer in the range \[1, 10000\].Example

```text
Example 1:	Input:  nums = [3, 4, 2]	Output:  6		Explanation:	Delete 4 to earn 4 points, consequently 3 is also deleted.	Then, delete 2 to earn 2 points. 6 total points are earned.	Example 2:	Input: nums = [2, 2, 3, 3, 3, 4]	Output:  9		Explanation:	Delete 3 to earn 3 points, deleting both 2's and the 4.	Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.	9 total points are earned.
```

## Solution 

Similar to [House Robber 392 \(M\)](house-robbe-392-m.md), just think of counter \(how many times that number appearance\) as houses, and the house's value equals to counter\[i\] \* i. Moreover, have to construct the entire counter list \(0 ~ 10001\), then we can follow the same policy as House Robber

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def deleteAndEarn(self, nums):
        # write your code here
        counter = [0 for _ in range(10001)]
        for num in nums:
            counter[num]+=1
        
        # dp[i] means the maximum value can get when deleting number no larger than i
        dp = [0 for _ in range(10001)]
        dp[1] = counter[1] 

        for i in range(2, 10001):
            dp[i] = max(dp[i - 1], dp[i - 2] + i * counter[i])
        return dp[i]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

