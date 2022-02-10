# Longest Mountain in Array (LeetCode 845) (M)

## Problem

****

You may recall that an array `arr` is a **mountain array** if and only if:

* `arr.length >= 3`
* There exists some index `i` (**0-indexed**) with `0 < i < arr.length - 1` such that:
  * `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
  * `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given an integer array `arr`, return _the length of the longest subarray, which is a mountain_. Return `0` if there is no mountain subarray.

&#x20;

**Example 1:**

```
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
```

**Example 2:**

```
Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.
```

&#x20;

**Constraints:**

* `1 <= arr.length <= 104`
* `0 <= arr[i] <= 104`

&#x20;

**Follow up:**

* Can you solve it using only one pass?
* Can you solve it in `O(1)` space?



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        base = 0
        ans = 0
        while base < len(arr):
            end = base
            if end + 1 < len(arr) and arr[end] < arr[end + 1]:
                # uphill
                while end + 1 < len(arr) and arr[end] < arr[end + 1]:
                    end+=1
                
                # check if end is on the peak
                # downhill
                if end + 1 < len(arr) and arr[end] > arr[end + 1]:
                    while end + 1 < len(arr) and arr[end] > arr[end + 1]:
                        end+=1
                    ans = max(ans, end - base + 1)
            base = max(end, base + 1)
        return ans
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

****
