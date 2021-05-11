# Top K Frequent Elements 1281 \(M\)

## Problem

Description

Given a non-empty array of integers, return the **k** most frequent elements.

* You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
* Your algorithm's time complexity **must be** better than O\(n log n\), where n is the array's size.

Example

**Example 1:**

```text
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**

```text
Input: nums = [1], k = 1
Output: [1]
```

## Solution - Hash + Sort \(Brute Force\)

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        # Write your code here
        cnt = {}
        # Time: O(n), Space: O(n)
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        keys_vals = [(key, val) for key, val in cnt.items()]
        # Time: O(nlogn), Space: O(n)
        keys_vals.sort(reverse = True, key = lambda n : n[1])
        return [key for key, val in keys_vals[:k]]
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(nlogn\)**
  * Hash Traverse: O\(n\)
  * Sort: O\(nlogn\)
* **Space Complexity: O\(2n\)**
  * Hash: O\(n\)
  * Tuple: O\(n\)

\*\*\*\*

## Solution - Heap

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

\*\*\*\*

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

