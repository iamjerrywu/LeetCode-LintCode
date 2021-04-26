# First Unique Number in Data Stream 685 \(M\)

## Problem

Given a continuous stream of data, write a function that returns the first unique number \(including the last number\) when the terminating number arrives. If the terminating number is not found, return `-1`.Example

**Example1**

```text
Input: 
[1, 2, 2, 1, 3, 4, 4, 5, 6]
5
Output: 3
```

**Example2**

```text
Input: 
[1, 2, 2, 1, 3, 4, 4, 5, 6]
7
Output: -1
```

**Example3**

```text
Input: 
[1, 2, 2, 1, 3, 4]
3
Output: 3
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        counter = {}

        is_break = False
        # first loop to set up hashmap, count all the num appearance before number
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if num == number:
                is_break = True
                break
        if not is_break:
            return -1
        
        # second loop, pop out the first number that only appear once 
        for num in nums:
            if counter[num] == 1:
                return num
            if num == number:
                return -1
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

