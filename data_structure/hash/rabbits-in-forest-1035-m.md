# Rabbits in Forest 1035 \(M\)

## Problem

In a forest, each rabbit has a color. Some of rabbits \(possibly all of them\) will tell you how many other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

1. The giver array will have length at most `1000`.
2. Each element in the array will be an integer in the range `[0, 999]`.

Example

**Example 1:**

```text
Input: [1, 1, 2]
Output: 5
Explanation:
  The two rabbits that answered "1" could both be the same color, say red.
  The rabbit than answered "2" can't be red or the answers would be inconsistent.
  Say the rabbit that answered "2" was blue.
  Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
  The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
```

**Example 2:**

```text
Input: [10, 10, 10]
Output: 11
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param answers: some subset of rabbits (possibly all of them) tell 
    @return: the minimum number of rabbits that could be in the forest.
    """
    def numRabbits(self, answers):
        # write your code here
        d = dict()
        for i in range(len(answer)):
            if answers[i] in d:
                d[answers[i]] = d[answers[i]] + 1
            else:
                d[answers[i]] = 1
        
        rabiit_num = 0
                
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

