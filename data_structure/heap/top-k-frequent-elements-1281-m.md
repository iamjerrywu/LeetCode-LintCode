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

## Solution - Heap \(1\)

### Code

{% tabs %}
{% tab title="python" %}
```python
import heapq
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
        
        # Time: O(n*logk), Space: O(n)
        # The heap remained k size, and traverse those n elements and do heappushpop one at a time (each takes O(logk) times)
        # so the time complexity is O(n*logk)
        return heapq.nlargest(k, cnt.keys(), key = cnt.get)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(nlogk\)**
* **Space Complexity: O\(n + k\)**

## Solution - Heap \(2\)

### Code

{% tabs %}
{% tab title="python" %}
```python
import heapq
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
        res = []
        for val, cnt in cnt.items():
            # since python default heap act as min heap
            # so those smaller cnt would on the top
            heapq.heappush(res, (cnt, val))
            if len(res) > k:
                # pop out those least frequent elements out
                heapq.heappop(res)
        return [val for count, val in res]
        

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(nlogk\)**
* **Space Complexity: O\(n + k\)**

## Solution - Quick Select

### Code

{% tabs %}
{% tab title="python" %}
```python
import heapq
class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        # Write your code here
        cnt = collections.Counter(nums)
        keys = list(cnt.keys())
        self.quick_select(keys, cnt, 0, len(keys) - 1, k)
        return keys[:k]
    
    def quick_select(self, keys, cnt, start, end, k):
        left, right = start, end
        if left >= right:
            return
        pivot = cnt[keys[(left + right)//2]]
        while left <= right:
            while left <= right and cnt[keys[left]] > pivot:
                left+=1
            while left <= right and cnt[keys[right]] < pivot:
                right-=1
            if left <= right:
                keys[left], keys[right] = keys[right], keys[left]
                left+=1
                right-=1
        if k - 1 <= right:
            return self.quick_select(keys, cnt, start, right, k)
        if k - 1 >= left:
            return self.quick_select(keys, cnt, left, end, k)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\) ~ O\(n^2\)**
  * Best: O\(n\)
  * Worst: O\(n^2\)
* **Space Complexity: O\(n\)**

