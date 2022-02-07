# Beautiful Array (LeetCode 932) (M)

## Problem

An array `nums` of length `n` is **beautiful** if:

* `nums` is a permutation of the integers in the range `[1, n]`.
* For every `0 <= i < j < n`, there is no index `k` with `i < k < j` where `2 * nums[k] == nums[i] + nums[j]`.

Given the integer `n`, return _any **beautiful** array_ `nums` _of length_ `n`. There will be at least one valid answer for the given `n`.

&#x20;

**Example 1:**

```
Input: n = 4
Output: [2,1,4,3]
```

**Example 2:**

```
Input: n = 5
Output: [3,1,2,5,4]
```

&#x20;

**Constraints:**

* `1 <= n <= 1000`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        
        # A = [1,3,2] is a beautiful array
        # A * 2 = [2, 6, 4] is still a beautiful array
        # A * 2 - 1 = [1, 5, 3] is still a beautiful array
        
        # moreover, if we put odd beautiful array in first half, even beautiful array in second half
        # then we can still get a beautiful array
        
        res = [1]
        while len(res) < n:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
            
        return [i for i in res if i <= n]
       
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
* **Space Complexity**
