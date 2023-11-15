# Race Car (LeetCode 818)

## Problem



Your car starts at position `0` and speed `+1` on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions `'A'` (accelerate) and `'R'` (reverse):

* When you get an instruction `'A'`, your car does the following:
  * `position += speed`
  * `speed *= 2`
*   When you get an instruction `'R'`, your car does the following:

    * If your speed is positive then `speed = -1`
    * otherwise `speed = 1`

    Your position stays the same.

For example, after commands `"AAR"`, your car goes to positions `0 --> 1 --> 3 --> 3`, and your speed goes to `1 --> 2 --> 4 --> -1`.

Given a target position `target`, return _the length of the shortest sequence of instructions to get there_.

&#x20;

**Example 1:**

<pre><code>Input: target = 3
<strong>Output:
</strong> 2
<strong>Explanation:
</strong> 
The shortest instruction sequence is "AA".
Your position goes from 0 --> 1 --> 3.
</code></pre>

**Example 2:**

<pre><code>Input: target = 6
<strong>Output:
</strong> 5
<strong>Explanation:
</strong> 
The shortest instruction sequence is "AAARA".
Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.
</code></pre>

&#x20;

**Constraints:**

* `1 <= target <= 104`



## Solution - BFS

{% tabs %}
{% tab title="Python" %}
```python
from collections import deque
ACTIONS = ['A', 'R']
class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        visited = set([(0, 1)])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                pos, speed = queue.popleft()
                if pos == target:
                    return steps
                for act in ACTIONS:
                    if act == 'A':
                        nxt_pos = pos + speed
                        speed*=2
                        if (nxt_pos, speed) not in visited:
                            visited.add((nxt_pos, speed))
                            queue.append((nxt_pos, speed))
                    elif act == 'R':
                        if speed < 0:
                            speed = 1
                        else:
                            speed=-1
                        if (pos, speed) not in visited:
                            visited.add((pos, speed))
                            queue.append((pos, speed))
            steps+=1
        return steps
        
        
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

* **Time Complexity:**
* **Space Complexity:**



## Solution - BFS Greedy Prunning

{% tabs %}
{% tab title="Python" %}
```python
from collections import deque
ACTIONS = ['A', 'R']
class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        visited = set([(0, 1)])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                pos, speed = queue.popleft()
                if pos == target:
                    return steps
                for act in ACTIONS:
                    if act == 'A':
                        nxt_pos = pos + speed
                        speed*=2
                        if (nxt_pos, speed) not in visited:
                            visited.add((nxt_pos, speed))
                            queue.append((nxt_pos, speed))
                    elif act == 'R':
                        if speed < 0:
                            nxt_speed = 1
                        else:
                            nxt_speed=-1
                        if (pos, nxt_speed) not in visited and ((pos + speed > target and speed > 0) or (pos + speed < target and speed < 0)):
                            visited.add((pos, nxt_speed))
                            queue.append((pos, nxt_speed))
            steps+=1
        return steps
        
        
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

* **Time Complexity:**
* **Space Complexity:**

