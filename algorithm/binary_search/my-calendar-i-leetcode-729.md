# My Calendar I (LeetCode 729)

## Problem

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a **double booking**.

A **double booking** happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers `start` and `end` that represents a booking on the half-open interval `[start, end)`, the range of real numbers `x` such that `start <= x < end`.

Implement the `MyCalendar` class:

* `MyCalendar()` Initializes the calendar object.
* `boolean book(int start, int end)` Returns `true` if the event can be added to the calendar successfully without causing a **double booking**. Otherwise, return `false` and do not add the event to the calendar.

&#x20;

**Example 1:**

<pre><code>Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
<strong>Output
</strong>[null, true, false, true]
<strong>Explanation
</strong>MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
</code></pre>

&#x20;

**Constraints:**

* `0 <= start < end <= 109`
* At most `1000` calls will be made to `book`.

## Solution - Brute Force

{% tabs %}
{% tab title="Python" %}
```python
class MyCalendar:

    def __init__(self):
        self.books = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.books:
            if s < end and start < e:
                return False
        self.books.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
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

* **Time Complexity: O(n^2)**
* **Space Complexity:**



## Solution - Binary Search

{% tabs %}
{% tab title="Python" %}
```python
from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.books = SortedList()

    def book(self, start: int, end: int) -> bool:
        if self.books:
            idx = self.search(start)
            # print(idx, len(self.books))
            if idx == -1:
                if self.books[-1][1] > start:
                    return False
            else:
                if self.books[idx][0] < end or (idx > 0 and self.books[idx - 1][1] > start):
                    return False
        self.books.add((start, end))
        return True
    
    def search(self, tar):
        if not self.books:
            return 0
        start, end = 0, len(self.books) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            
            if self.books[mid][0] <= tar:
                start = mid
            elif self.books[mid][0] > tar:
                end = mid
        
        if self.books[start][0] > tar:
            return start
        if self.books[end][0] > tar:
            return end
        return -1

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
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

* **Time Complexity: O(nlogn)**
* **Space Complexity:**
