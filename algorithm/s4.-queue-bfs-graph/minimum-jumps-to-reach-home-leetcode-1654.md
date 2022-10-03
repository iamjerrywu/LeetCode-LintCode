# Minimum Jumps to Reach Home (LeetCode 1654)

## Problem

****

A certain bug's home is on the x-axis at position `x`. Help them get there from position `0`.

The bug jumps according to the following rules:

* It can jump exactly `a` positions **forward** (to the right).
* It can jump exactly `b` positions **backward** (to the left).
* It cannot jump backward twice in a row.
* It cannot jump to any `forbidden` positions.

The bug may jump forward **beyond** its home, but it **cannot jump** to positions numbered with **negative** integers.

Given an array of integers `forbidden`, where `forbidden[i]` means that the bug cannot jump to the position `forbidden[i]`, and integers `a`, `b`, and `x`, return _the minimum number of jumps needed for the bug to reach its home_. If there is no possible sequence of jumps that lands the bug on position `x`, return `-1.`

&#x20;

**Example 1:**

<pre><code>Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
<strong>Output:
</strong> 3
<strong>Explanation:
</strong> 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.</code></pre>

**Example 2:**

<pre><code>Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
<strong>Output:
</strong> -1</code></pre>

**Example 3:**

<pre><code>Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.</code></pre>

&#x20;

**Constraints:**

* `1 <= forbidden.length <= 1000`
* `1 <= a, b, forbidden[i] <= 2000`
* `0 <= x <= 2000`
* All the elements in `forbidden` are distinct.
* Position `x` is not forbidden.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
from collections import deque
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        if x in forbidden:
            return -1
        queue = deque([(0, 1)])
        
        visited = set()
        steps = 0
        while queue:
            for _ in range(len(queue)):
                pos, b_cnt = queue.popleft()
                if pos == x:
                    return steps
                # jump forward
                fwd_pos = pos + a
                if fwd_pos <= 20000 and fwd_pos not in forbidden and (fwd_pos, 1) not in visited:
                    visited.add((fwd_pos, 1))
                    queue.append((fwd_pos, 1))
                    
                # jump backward
                bck_pos = pos - b
                if b_cnt > 0 and bck_pos >= 0 and bck_pos not in forbidden and (bck_pos, b_cnt - 1) not in visited:
                    visited.add((bck_pos, b_cnt - 1))
                    queue.append((bck_pos, b_cnt - 1))
            steps+=1
        return -1
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(2n)**
* **Space Complexity: O(n)**

