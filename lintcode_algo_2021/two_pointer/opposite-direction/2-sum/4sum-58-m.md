# 4Sum 58 \(M\)

## Problem

Given an array _S_ of _n_ integers, are there elements _a_, _b_, _c_, and _d_ in _S_ such that _a + b + c + d = target_?

Find all unique quadruplets in the array which gives the sum of target.

Elements in a quadruplet \(_a,b,c,d_\) must be in non-descending order. \(ie, _a ≤ b ≤ c ≤ d_\)  
The solution set must not contain duplicate quadruplets.Example

Example 1:

```text
Input:[2,7,11,15],3
Output:[]

```

Example 2:

```text
Input:[1,0,-1,0,-2,2],0
Output:
[[-1, 0, 0, 1]
,[-2, -1, 1, 2]
,[-2, 0, 0, 2]]
```

## Solution



### Code - Two Pointer

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        res = []
        if len(numbers) < 4:
            return res
        numbers.sort()

        for i in range(0, len(numbers) - 3):
            # skip duplicate
            if i > 0 and numbers[i - 1] == numbers[i]:
                continue
            for j in range(len(numbers) - 1, i + 2, -1):
                # skip duplicate
                if j + 1 < len(numbers) and numbers[j + 1] == numbers[j]:
                    continue
                base = target - (numbers[i] + numbers[j])
                left, right = i + 1, j - 1
                while left < right:
                    if numbers[left] + numbers[right] < base:
                        left+=1
                    elif numbers[left] + numbers[right] > base:
                        right-=1
                    else:
                        res.append([numbers[i], numbers[left], numbers[right], numbers[j]])
                        left+=1
                        right-=1
                        # skip duplicate
                        while left < right and numbers[left - 1] == numbers[left]:
                            left+=1
                        while left < right and numbers[right + 1] == numbers[right]:
                            right-=1
        return res

```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^3\)**
* **Space Complexity: O\(1\)**

