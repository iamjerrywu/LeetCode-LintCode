# Pick Apples 1850 \(M\)

## Problem

Alice and Bob work in a beautiful orchard. There are N apple trees in the orchard. The apple trees are arranged in a row and they are numbered from 1 to N.  
Alice is planning to collect all the apples from K consecutive trees and Bob is planning to collect all the apples from L consecutive trees.  
They want to choose to disjoint segements \(one consisting of K trees of Alice and the other consisting of L trees for Bob\) so as not to disturb each other. you should return the maximum number of apples that they can collect.

* N is an integer within the range: \[2, 600\]
* K and L are integers within the range: \[1, N - 1\]
* each element of array A is an integer within the range: \[1, 500\]

Example

**Example 1:**

```text
input:
A = [6, 1, 4, 6, 3, 2, 7, 4]
K = 3
L = 2
Output: 
24
Explanation: 
beacuse Alice can choose tree 3 to 5 and collect 4 + 6 + 3 = 13 apples, and Bob can choose trees 7 to 8 and collect 7 + 4 = 11 apples.Thus, they will collect 13 + 11 = 24.
```

**Example 2:**

```text
Input:
A = [10, 19, 15]
K = 2
L = 2
Output: 
-1
Explanation: 
beacause it is not possible for Alice and Bob to choose two disjoint intervals.
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

