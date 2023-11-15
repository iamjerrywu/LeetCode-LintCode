---
description: LinkedIn
---

# Can Place Flowers 1138 (E)

## Problem

Suppose you have a long flowerbed in which some of the pots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number **n**, return if **n** new flowers can be planted in it without violating the no-adjacent-flowers rule.

1.The input array won't violate no-adjacent-flowers rule.\
2.The input array size is in the range of \[1, 20000].\
3.n is a non-negative integer which won't exceed the input array size.Example

**Example1**

```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
```

**Example2**

```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
```

## Solution&#x20;

### Code

{% tabs %}
{% tab title="python(1)" %}
```python
class Solution:
    """
    @param flowerbed: an array
    @param n: an Integer
    @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
    """
    def canPlaceFlowers(self, flowerbed, n):
        # Write your code here
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed
        return n <= 0
```
{% endtab %}

{% tab title="python(2)" %}
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:  
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # head
                if i == 0 and (len(flowerbed) == 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n-=1
                # tail
                elif i == len(flowerbed) - 1 and (len(flowerbed) == 1 or flowerbed[i - 1] == 0):
                    flowerbed[i] = 1
                    n-=1
                # middle points
                elif i + 1 < len(flowerbed) and flowerbed[i + 1] == 0 and i - 1 >= 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0
                
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**



## Solution -Greedy

Adding zero to head and tail of original flowerbed list

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_flowerbed = []
        new_flowerbed.append(0)
        for val in flowerbed:
            new_flowerbed.append(val)
        new_flowerbed.append(0)
        
        for i in range(1, len(new_flowerbed) - 1):
            if new_flowerbed[i] == 0 and new_flowerbed[i - 1] != 1 and new_flowerbed[i + 1] != 1:
                new_flowerbed[i] = 1
                n-=1
        return n <= 0
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
