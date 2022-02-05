# Reorganize String 1041 (M)

## Problem

Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same.

Return _any possible rearrangement of_ `s` _or return_ `""` _if not possible_.

**Example 1:**

```
Input: s = "aab"
Output: "aba"
```

**Example 2:**

```
Input: s = "aaab"
Output: ""
```

**Constraints:**

* `1 <= s.length <= 500`
* `s` consists of lowercase English letters.

## Solution

{% tabs %}
{% tab title="Python" %}
```python
import heapq
import collections
class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = collections.Counter(s)
        rec = []
        for k, v in cnt.items():
            rec.append([-v, k])
        
        heapq.heapify(rec)
        
        copy_rec = []
        ans = []
        while len(rec) > 1:
            first = heapq.heappop(rec)
            ans.append(first[1])
            val1 = -first[0] - 1
            
            if len(rec):
                sec = heapq.heappop(rec)
                ans.append(sec[1])
                val2 = -sec[0] - 1
                
                if val2 > 0:
                    heapq.heappush(rec, [-val2, sec[1]])
            
            if val1 > 0:
                heapq.heappush(rec, [-val1, first[1]])
            
        
        #last chr
        if len(rec):
            if -rec[0][0] > 1:
                return ''
            else:
                return (''.join(ans)) + rec[0][1]
        return ''.join(ans)
```
{% endtab %}

{% tab title="Python (Better)" %}
```python
import heapq
import collections
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        heap = []
        count = collections.Counter(s)
        
        for k, v in count.items():
            heapq.heappush(heap, [-v, k])
        
        ans = ""
        while heap:
            # first pop
            cnt1, c1 = heapq.heappop(heap)
            ans+=c1
            cnt1 = abs(cnt1) - 1
            if len(heap) == 0 and cnt1 > 0:
                return ""
            
            # second pop
            if heap:
                cnt2, c2 = heapq.heappop(heap)
                ans+=c2
                cnt2 = abs(cnt2) - 1
            if cnt1 > 0:
                heapq.heappush(heap, [-cnt1, c1])
            if cnt2 > 0:
                heapq.heappush(heap, [-cnt2, c2])
        return ans
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**
