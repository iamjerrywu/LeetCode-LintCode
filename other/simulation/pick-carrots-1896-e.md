# Pick Carrots 1896 \(E\)

## Problem

Given a n \* m matrix **carrot** , carrot\[i\]\[j\] denotes the number of carrots at coordinates \(i, j\) .  
Starting from the center of the matrix, moving in the direction of the largest number of carrots in the four directions, guarantee that the direction of movement is unique.  
Return the number of carrot you can get.

* n and m within the range is: \[1, 300\]
* carrot\[i\]\[j\] within the range is: \[1, 20000\]
* The central point is rounded down, such as n = 4, m = 4, so the start point is \(1, 1\)
* If there are no carrots around, stop moving.

Example

```text
Example 1:
Input:
carrot = 
[[5, 7, 6, 3],
[2,  4, 8, 12],
[3, 5, 10, 7],
[4, 16, 4, 17]]
Output: 
83
Explanation: 
start point is (1, 1), moving route is 4 -> 8 -> 12 -> 7 -> 17 -> 4 -> 16 -> 5 -> 10
```

```text
Example 2:
Input:
carrot = 
[[5, 3, 7, 1, 7],
 [4, 6, 5, 2, 8],
 [2, 1, 1, 4, 6]]
 Output: 
 30
 Explanation: 
 start point is (1, 2), moving route is: 5 -> 7 -> 3 -> 6 -> 4 -> 5
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

