# Product of Array Except Self 1310 \(M\)

## Problem

Given an array of n integers where n &gt; 1, `nums`, return an array output such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

Solve it **without division** and in O\(n\).Example

**Example1**

```text
Input: [1,2,3,4]
Output: [24,12,8,6]
Explanation:
2*3*4=24
1*3*4=12
1*2*4=8
1*2*3=6
```

**Example2**

```text
Input: [2,3,8]
Output: [24,16,6]
Explanation:
3*8=24
2*8=16
2*3=6
```

Challenge

Could you solve it with constant space complexity? \(Note: The output array does not count as extra space for the purpose of space complexity analysis.\)

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        # write your code here
        length = len(nums)
        result = [1] * length
        prefix_product = 1
        postfix_product= 1

        for i in range(length):
            result[i] *= prefix_product
            prefix_product *= nums[i]
        
        for i in range(length - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        
        return result
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

