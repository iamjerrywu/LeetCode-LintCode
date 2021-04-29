# Second Max Array 479 \(E\)

## Problem

Description

Find the second max number in a given array.

You can assume the array contains at least two numbers.  
The second max number is the second number in a descending array.Example

Example1:

```text
Input: [1,3,2,4]
Output: 3
```

Example2:

```text
Input: [1,1,2,2]
Output: 
```

## Solution - First, Second Comparison

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        # write your code here
        if len(nums) < 2:
            return 0
        first, second = max(nums[0], nums[1]),min(nums[0], nums[1])
        for i in range(2, len(nums)):
            if nums[i] > first:
                second = first
                first = nums[i]
            elif nums[i] > second:
                second = nums[i]
        return second
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity:**

\*\*\*\*

## Solution - Sorting

### Code

{% tabs %}
{% tab title="python" %}
```python

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

\*\*\*\*

## Solution - 

### Code

{% tabs %}
{% tab title="python" %}
```python

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

