# Minimum Deletion Cost to Avoid Repeating Letters (LeetCode1578) (M)

## Problem



Given a string `s` and an array of integers `cost` where `cost[i]` is the cost of deleting the `ith` character in `s`.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

&#x20;

**Example 1:**

```
Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
```

**Example 2:**

```
Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.
```

**Example 3:**

```
Input: s = "aabaa", cost = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character, getting the string ("aba").
```

&#x20;

**Constraints:**

* `s.length == cost.length`
* `1 <= s.length, cost.length <= 10^5`
* `1 <= cost[i] <= 10^4`
* `s` contains only lowercase English letters.



## Solution&#x20;

![](<../../.gitbook/assets/Screen Shot 2021-11-29 at 1.05.54 PM.png>)



{% tabs %}
{% tab title="Python" %}
```python
import heapq
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        heap = []
        
        ptr = 0
        ans = 0
        while ptr + 1 < len(s):
            if s[ptr] == s[ptr + 1]:
                while ptr + 1 < len(s) and s[ptr] == s[ptr + 1]:
                    heapq.heappush(heap, cost[ptr])
                    ptr+=1
                heapq.heappush(heap, cost[ptr])
            
                while len(heap) > 1:
                    ans+=heapq.heappop(heap)
                # remained one, but need to empty the heap as well
                heapq.heappop(heap)
            
            ptr+=1
        return ans            
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
  * n: len(s)
* **Space Complexity:**
