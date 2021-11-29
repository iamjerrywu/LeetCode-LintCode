# Reconstruct Itinerary (LeetCode 332) (M)

```
    ans = []
    self.dfs('JFK', dests, ans)
    
    return ans[::-1]

def dfs(self, start, dests, ans):
    while len(dests[start]) > 0:
        dest = heapq.heappop(dests[start])
        self.dfs(dest, dests, ans)
    # if run out of destinations, it means this points is actually the final destination
    ans.append(start)
    
    
    
    
```

import heapq import collections class Solution: def findItinerary(self, tickets: List\[List\[str]]) -> List\[str]: dests = collections.defaultdict(list) for ticket in tickets: heapq.heappush(dests\[ticket\[0]], ticket\[1])

## Problem

&#x20;

You are given a list of airline `tickets` where `tickets[i] = [fromi, toi]` represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from `"JFK"`, thus, the itinerary must begin with `"JFK"`. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

* For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg)

```
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg)

```
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
```

&#x20;

**Constraints:**

* `1 <= tickets.length <= 300`
* `tickets[i].length == 2`
* `fromi.length == 3`
* `toi.length == 3`
* `fromi` and `toi` consist of uppercase English letters.
* `fromi != toi`

## Solution - DFS + Greedy

{% tabs %}
{% tab title="Python" %}
```python
import heapq
import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dests = collections.defaultdict(list)
        for ticket in tickets:
            heapq.heappush(dests[ticket[0]], ticket[1])
        
        ans = []
        self.dfs('JFK', dests, ans)
        
        return ans[::-1]
    
    def dfs(self, start, dests, ans):
        while len(dests[start]) > 0:
            dest = heapq.heappop(dests[start])
            self.dfs(dest, dests, ans)
        # if run out of destinations, it means this points is actually the final destination
        ans.append(start)
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
