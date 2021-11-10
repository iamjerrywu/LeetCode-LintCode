# Task Scheduler 945 (M)

## Problem

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval `n` that means between two `same tasks`, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the `least` number of intervals the CPU will take to finish all the given tasks.

1. The number of tasks is in the range `[1, 10000]`.
2. The integer n is in the range `[0, 100]`.

Example

**Example1**

```
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B.
```

**Example2**

```
Input: tasks = ['A','A','A','B','B','B'], n = 1
Output: 6
Explanation:
A -> B -> A -> B -> A -> B.
```

## Solution - Greedy

The total number of CPU intervals we need consists of busy and idle slots. Number of busy slots is defined by the number of tasks to execute: `len(tasks)`. The problem is to compute a number of idle slots.

Maximum possible number of idle slots is defined by the frequency of the most frequent task: `idle_time <= (f_max - 1) * n`.

![fig](https://leetcode.com/problems/task-scheduler/Figures/621/idle.png)

This maximum could be decreased because one doesn't need to keep the CPU idle during cooling periods. It could execute different tasks as well.

To compute the minimum number of idle slots, one could use a greedy strategy. The idea is to sort the tasks by frequency in the descending order and fulfill as many idle slots as one could.

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # write your code here
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')]+=1
        
        frequencies.sort()

        max_freq = frequencies.pop()
        idle_time = (max_freq - 1) * n

        while frequencies and idle_time > 0:
            idle_time-=min(max_freq - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
  * n: the totals amount of tasks need to be executed
* **Space Complexity: O(1)**

****

## Solution - Math



**ntuition**

Let's use some math to _compute_ the answer. There are two possible situations:

* The most frequent task is not frequent enough to force the presence of idle slots.

![fig](https://leetcode.com/problems/task-scheduler/Figures/621/all2.png)

* The most frequent task is frequent enough to force some idle slots.

![fig](https://leetcode.com/problems/task-scheduler/Figures/621/frequent2.png)

> The answer is the maximum between these two.

The first situation is straightforward because the total number of slots is defined by the number of tasks: `len(tasks)`.

The second situation is a bit more tricky and requires to know the number `n_max` and the frequency `f_max` of the most frequent tasks.

![fig](https://leetcode.com/problems/task-scheduler/Figures/621/f\_max.png)

Now it's easy to compute:

![fig](https://leetcode.com/problems/task-scheduler/Figures/621/compute.png)

**Algorithm**

* The maximum number of tasks is 26. Let's allocate an array `frequencies` of 26 elements to keep the frequency of each task.
* Iterate over the input array and store the frequency of task A at index 0, the frequency of task B at index 1, etc.
* Find the maximum frequency: `f_max = max(frequencies)`.
* Find the number of tasks which have the max frequency: `n_max = frequencies.count(f_max)`.
* If the number of slots to use is defined by the most frequent task, it's equal to `(f_max - 1) * (n + 1) + n_max`.
* Otherwise, the number of slots to use is defined by the overall number of tasks: `len(tasks)`.
* Return the maximum of these two: `max(len(tasks), (f_max - 1) * (n + 1) + n_max)`.



### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # write your code here
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')]+=1
        max_freq = max(frequencies)
        max_freq_cnt = frequencies.count(max_freq)

        return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_cnt)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
  * n: the totals amount of tasks need to be executed
* **Space Complexity: O(1)**
