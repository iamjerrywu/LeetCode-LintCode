# Three Sum 57 \(M\)

## Problem

Given an array _S_ of n integers, are there elements _a_, _b_, _c_ in _S_ such that `a + b + c = 0`? Find all unique triplets in the array which gives the sum of zero.

Elements in a triplet \(a,b,c\) must be in non-descending order. \(ie, a ≤ b ≤ c\)

The solution set must not contain duplicate triplets.Example

**Example 1:**

```text
Input:[2,7,11,15]
Output:[]
```

**Example 2:**

```text
Input:[-1,0,1,2,-1,-4]
Output:	[[-1, 0, 1],[-1, -1, 2]]
```

## Solution

The second and third element add up should equal to the first elements

Note that to take the duplicated number that shouldn't be visited twice! 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        res = []
        if len(numbers) < 3:
            return res
        numbers.sort()

        for b in range(0, len(numbers) - 2):
            # skip the first duplicated number as base
            if b > 0 and numbers[b - 1] == numbers[b]:
                continue
            base = -numbers[b]
            i, j = b + 1, len(numbers) - 1
            while i < j:
                if numbers[i] + numbers[j] < base:
                    i+=1
                elif numbers[i] + numbers[j] > base:
                    j-=1
                else:
                    res.append([-base, numbers[i], numbers[j]])
                    i+=1
                    j-=1
                    # skip the duplicated element
                    while i < j and numbers[i - 1] == numbers[i]:
                        i+=1
                    while i < j and numbers[j + 1] == numbers[j]:
                        j-=1
        return res

```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^2\)**
* **Space Complexity:**

