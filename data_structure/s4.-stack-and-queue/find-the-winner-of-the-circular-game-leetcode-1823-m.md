# Find the Winner of the Circular Game (LeetCode 1823) (M)

## Problem

There are `n` friends that are playing a game. The friends are sitting in a circle and are numbered from `1` to `n` in **clockwise order**. More formally, moving clockwise from the `ith` friend brings you to the `(i+1)th` friend for `1 <= i < n`, and moving clockwise from the `nth` friend brings you to the `1st` friend.

The rules of the game are as follows:

1. **Start** at the `1st` friend.
2. Count the next `k` friends in the clockwise direction **including** the friend you started at. The counting wraps around the circle and may count some friends more than once.
3. The last friend you counted leaves the circle and loses the game.
4. If there is still more than one friend in the circle, go back to step `2` **starting** from the friend **immediately clockwise** of the friend who just lost and repeat.
5. Else, the last friend in the circle wins the game.

Given the number of friends, `n`, and an integer `k`, return _the winner of the game_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/25/ic234-q2-ex11.png)

<pre><code>Input: n = 5, k = 2
<strong>Output:
</strong> 3
<strong>Explanation:
</strong> Here are the steps of the game:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the circle. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4.
5) Friend 4 leaves the circle. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1.
7) Friend 1 leaves the circle. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.</code></pre>

**Example 2:**

<pre><code>Input: n = 6, k = 5
<strong>Output:
</strong> 1
<strong>Explanation:
</strong> The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.</code></pre>

&#x20;

**Constraints:**

* `1 <= k <= n <= 500`

&#x20;

**Follow up:**

Could you solve this problem in linear time with constant space?



## Solution&#x20;

<figure><img src="../../.gitbook/assets/Screen Shot 2022-10-17 at 11.49.05 AM.png" alt=""><figcaption></figcaption></figure>

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()
        for i in range(1, n + 1):
            queue.append(i)
        
        while len(queue) != 1:
            for _ in range(1, k):
                queue.append(queue.popleft())
            queue.popleft()
        
        return queue.popleft()
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
