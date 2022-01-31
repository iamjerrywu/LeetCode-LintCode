# Friends of Appropriate Ages (LeetCode 825) (M)

## Problem

There are `n` persons on a social media website. You are given an integer array `ages` where `ages[i]` is the age of the `ith` person.

A Person `x` will not send a friend request to a person `y` (`x != y`) if any of the following conditions is true:

* `age[y] <= 0.5 * age[x] + 7`
* `age[y] > age[x]`
* `age[y] > 100 && age[x] < 100`

Otherwise, `x` will send a friend request to `y`.

Note that if `x` sends a request to `y`, `y` will not necessarily send a request to `x`. Also, a person will not send a friend request to themself.

Return _the total number of friend requests made_.

&#x20;

**Example 1:**

```
Input: ages = [16,16]
Output: 2
Explanation: 2 people friend request each other.
```

**Example 2:**

```
Input: ages = [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
```

**Example 3:**

```
Input: ages = [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
```

&#x20;

**Constraints:**

* `n == ages.length`
* `1 <= n <= 2 * 104`
* `1 <= ages[i] <= 120`

## Solution - Binary Search

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        ans = 0
        for i in range(len(ages)):
            age = ages[i]
            lower = self.search_first(ages, age/2 + 7)
            upper = self.search_last(ages, age)
            ans+=max(upper - lower, 0)
        return ans
    
    def search_last(self, arr, tar):
        start, end = 0, len(arr) - 1
        
        while start + 1 < end:
            mid = start + (end - start)//2
            
            if arr[mid] <= tar:
                start = mid
            else:
                end = mid
        if arr[end] == tar:
            return end
        if arr[start] == tar:
            return start
        return len(arr)
    
    def search_first(self, arr, tar):
        start, end = 0, len(arr) - 1
        
        while start + 1 < end:
            mid = start + (end - start)//2
            if arr[mid] <= tar:
                start = mid
            else:
                end = mid
        if arr[start] > tar:
            return start
        if arr[end] > tar:
            return end
        return len(arr)
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
  * **n: length of ages, can up to 2\*10000**
* **Space Complexity:**

## Solution - Hash

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = collections.Counter(ages)
        ans = 0
        for a1 in counter.keys():
            for a2 in counter.keys():
                if self.will_request(a1, a2):
                    if a1 == a2:
                        ans+=counter[a1] * (counter[a2] - 1)
                    else:
                        ans+=counter[a1] * counter[a2]
        return ans
    
    def will_request(self, a1, a2):
        return a2 > (a1/2 + 7) and a2 <= a1
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

* **Time Complexity: O(m^2)**
  * **m up to 120, the max age of ages**
* **Space Complexity:**

****

****
