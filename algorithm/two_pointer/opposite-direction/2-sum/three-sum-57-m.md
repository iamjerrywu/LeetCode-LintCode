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

```python
#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the triplets function below.

# find the first bigger than target index
def bi_search(target, arr):
    start, end = 0, len(arr) - 1
    
    while start + 1 < end:
        mid = start + (end - start)//2
        if arr[mid] > target:
            end = mid
        else:
            start = mid
    if arr[start] > target:
        return start
    if arr[end] > target:
        return end
    return -1

def find_three_sum(t, d):
    cnt = 0
    for b in range(0, len(d) - 2):
        base = d[b]
        for i in range(b + 1, len(d) - 1):
            j = bi_search(t - base - d[i], d[i + 1:])
            if j == -1:
                cnt+=len(d) - i - 1
                cnt+=0
            else:
                j = j + i + 1
                cnt+=j - i - 1
    return cnt
        
def triplets(t, d):
    
    d.sort()
    if len(d) < 3:
        return 0
    
    idx = bi_search(t - d[0] - d[1], d)
    if idx == -1:
        # if cannot find, means then entire list is smaller
        ans = find_three_sum(t, d)
    else:
        ans = find_three_sum(t, d[:idx + 1])
    return ans
    
    
if __name__ == '__main__':
```

