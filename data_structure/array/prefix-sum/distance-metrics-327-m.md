# Distance Metrics 327 \(M\)

## Problem

For each element in a given array, calculate the absolute value of index differences between it and all other elements of the same value. Return the resulting values in an array. For example, if the array elements at indices 2 and 3 are equal, the distance metric for element 2 is \|2-3\| = 1. For element 3 it is\|3-2\|=1.

1 \leq n \leq 10^51≤n≤105  
1 \leq a\[i\] \leq 10^91≤a\[i\]≤109Example

**Example 1:**

```text
Input:[1, 2, 1, 1, 2, 3]Output:[5, 3, 3, 4, 3, 0]Explanation:The element 0 = 1. Similar elements are at indices 2 and 3.The distance metric for element 0 = | 0 - 2 | + | 0 - 3 | = 5Similar logic follows:The distance metric for element 1 = | 1 - 4 | =3The distance metric for element 2 = | 2 - 0 | + | 2-3 | = 3The distance metric for element 3 = | 3 - 0 | + | 3 - 2 | = 4The distance metric for element 4 = | 4 - 1 | = 3The distance metric for element 5 = 0Thus, distance metrics=[5, 3, 3, 4, 3, 0]
```

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param a: an integer array
    @return: an integer array
    """
    def getDistanceMetrics(self, nums):
        res = [0 for _ in range(len(nums))]
        left = [0 for _ in range(len(nums))]
        right = [0 for _ in range(len(nums))]

        indexes = dict() # (num : (count, prev_index))
        for i, num in enumerate(nums):
            if num not in indexes:
                indexes[num] = (1, i)
            else:
                c, prev_id = indexes[num]
                left[i] = c * (i-prev_id) + left[prev_id]
                indexes[num] = (c + 1, i)

        indexes = dict() # (num : (count, prev_index))
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            if num not in indexes:
                indexes[num] = (1, i)
            else:
                c, prev_id = indexes[num]
                right[i] = c * (prev_id-i) + right[prev_id]
                indexes[num] = (c + 1, i)
        print(left)
        print(right)
        for i in range(len(nums)):
            res[i] = left[i] + right[i]

        return res
```
{% endtab %}
{% endtabs %}

* **Time Complexity:** 
* **Space Complexity:**

