# Copy Books II 438 \(H\)

## Problem

Given `n` books and each book has the same number of pages. There are `k` persons to copy these books and the `i-th` person needs `times[i]` minutes to copy a book.

Each person can copy any number of books and they start copying at the same time. What's the best strategy to assign books so that the job can be finished at the earliest time?

Return the shortest time.Example

**Example 1:**

```text
Input: n = 4, times = [3, 2, 4]
Output: 4
Explanation:
First person spends 3 minutes to copy 1 book.
Second person spends 4 minutes to copy 2 books.
Third person spends 4 minutes to copy 1 book.
```

**Example 2:**

```text
Input: n = 4, times = [3, 2, 4, 5]
Output: 4
Explanation: Use the same strategy as example 1 and the forth person does nothing.
```

## Solution - Binary Search

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copyBooksII(self, n, times):
        # write your code here
        if n == 0:
            return 0
        # can actually pick any time in times, but picking smallest can reduce search time
        time, total_time = 0, min(times) * n
        while time < total_time:
            print(time, total_time)
            mid = (time + total_time)//2
            if self.can_copy(n, times, mid):
                total_time = mid
            else:
                time = mid + 1
        return time
    
    def can_copy(self, n, times, mid):
        books = 0
        for time in times:
            books+=mid//time
        return books >= n

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(logx\)**
  * x = min\(times\) \* n
* **Space Complexity: O\(1\)**

