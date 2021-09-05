# The Number of Weak Characters in the Game \(LeetCode 1996\) \(M\)

## Problem

You are playing a game that contains multiple characters, and each of the characters has **two** main properties: **attack** and **defense**. You are given a 2D integer array `properties` where `properties[i] = [attacki, defensei]` represents the properties of the `ith` character in the game.

A character is said to be **weak** if any other character has **both** attack and defense levels **strictly greater** than this character's attack and defense levels. More formally, a character `i` is said to be **weak** if there exists another character `j` where `attackj > attacki` and `defensej > defensei`.

Return _the number of **weak** characters_.

**Example 1:**

```text
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.
```

**Example 2:**

```text
Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.
```

**Example 3:**

```text
Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
```

**Constraints:**

* `2 <= properties.length <= 105`
* `properties[i].length == 2`
* `1 <= attacki, defensei <= 105`

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x:(x[0], x[1]))
        print(properties)
        
        stack = []
        ans = 0
        
        for a, d in properties:
            while stack and stack[-1][0] < a and stack[-1][1] < d:
                stack.pop()
                ans+=1
            stack.append((a, d))
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(nlogn\)**
* **Space Complexity:** 

