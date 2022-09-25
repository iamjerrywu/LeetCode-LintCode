# Sort Integers by The Number of 1 Bits (LeetCode 1356) (E)

## Problem

You are given an integer array `arr`. Sort the integers in the array in ascending order by the number of `1`'s in their binary representation and in case of two or more integers have the same number of `1`'s you have to sort them in ascending order.

Return _the array after sorting it_.

&#x20;

**Example 1:**

<pre><code>Input: arr = [0,1,2,3,4,5,6,7,8]
<strong>Output:
</strong> [0,1,2,4,8,3,5,6,7]
<strong>Explantion:
</strong> [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]</code></pre>

**Example 2:**

<pre><code>Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
<strong>Output:
</strong> [1,2,4,8,16,32,64,128,256,512,1024]
<strong>Explantion:
</strong> All integers have 1 bit in the binary representation, you should just sort them in ascending order.</code></pre>

&#x20;

**Constraints:**

* `1 <= arr.length <= 500`
* `0 <= arr[i] <= 104`

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
import heapq
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        heap = []
        for num in arr:
            heapq.heappush(heap, [self.get_ones(num), num])
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans
    def get_ones(self, num):
        cnt=0
        while num:
            if num&0x1==1:
                num-=1
                cnt+=1
            num//=2
        return cnt
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
