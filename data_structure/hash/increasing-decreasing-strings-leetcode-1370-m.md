# Increasing Decreasing Strings (LeetCode 1370) (M)

## Problem



Given a string `s`. You should re-order the string using the following algorithm:

1. Pick the **smallest** character from `s` and **append** it to the result.
2. Pick the **smallest** character from `s` which is greater than the last appended character to the result and **append** it.
3. Repeat step 2 until you cannot pick more characters.
4. Pick the **largest** character from `s` and **append** it to the result.
5. Pick the **largest** character from `s` which is smaller than the last appended character to the result and **append** it.
6. Repeat step 5 until you cannot pick more characters.
7. Repeat the steps from 1 to 6 until you pick all characters from `s`.

In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return _the result string_ after sorting `s` with this algorithm.

**Example 1:**

```
Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
```

**Example 2:**

```
Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
```

**Example 3:**

```
Input: s = "leetcode"
Output: "cdelotee"
```

**Example 4:**

```
Input: s = "ggggggg"
Output: "ggggggg"
```

**Example 5:**

```
Input: s = "spo"
Output: "ops"
```

**Constraints:**

* `1 <= s.length <= 500`
* `s` contains only lower-case English letters.

## Solution - Heap

{% tabs %}
{% tab title="Python" %}
```python
import heapq
class Solution:
    def sortString(self, s: str) -> str:
        count = collections.Counter(s)
        
        inc_heap = []
        dec_heap = []
        
        for [k, v] in count.items():
            heapq.heappush(inc_heap, [ord(k), v])
        
        res = ''
        while inc_heap or dec_heap:
            while inc_heap:
                cur = heapq.heappop(inc_heap)
                res+=chr(cur[0])
                cur[1]-=1
                if cur[1] != 0:
                    heapq.heappush(dec_heap, [-cur[0], cur[1]])
            
            while dec_heap:
                cur = heapq.heappop(dec_heap)
                res+=chr(-cur[0])
                cur[1]-=1
                if cur[1] != 0:
                    heapq.heappush(inc_heap, [-cur[0], cur[1]])

        return res
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**

## Solution - Counter&#x20;

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def sortString(self, s: str) -> str:
        count = collections.Counter(s)
        inc = True
        res = ''
        while count:
            for c in sorted(count) if inc else reversed(sorted(count)):
                if count[c] > 0:
                    res+=c
                    count[c]-=1
                else:
                    del count[c]
            inc = not inc
        return res
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
