# Similar String Groups (LeetCode 839) (H)

## Problem

Two strings `X` and `Y` are similar if we can swap two letters (in different positions) of `X`, so that it equals `Y`. Also two strings `X` and `Y` are similar if they are equal.

For example, `"tars"` and `"rats"` are similar (swapping at positions `0` and `2`), and `"rats"` and `"arts"` are similar, but `"star"` is not similar to `"tars"`, `"rats"`, or `"arts"`.

Together, these form two connected groups by similarity: `{"tars", "rats", "arts"}` and `{"star"}`.  Notice that `"tars"` and `"arts"` are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list `strs` of strings where every string in `strs` is an anagram of every other string in `strs`. How many groups are there?



**Example 1:**

```
Input: strs = ["tars","rats","arts","star"]
Output: 2
```

**Example 2:**

```
Input: strs = ["omv","ovm"]
Output: 1
```



**Constraints:**

* `1 <= strs.length <= 300`
* `1 <= strs[i].length <= 300`
* `strs[i]` consists of lowercase letters only.
* All words in `strs` have the same length and are anagrams of each other.

## Solution - BFS

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        start = strs[0]
        connected  = collections.defaultdict(set)
        for i in range(len(strs) - 1):
            for j in range(1, len(strs)):
                if self.is_similar(strs[i], strs[j]):
                    connected[strs[i]].add(strs[j])
                    connected[strs[j]].add(strs[i])
        visited = set()
        ans = 0
       
        # because we are traversing all the string in strs, so those not belongs to connected groups
        # will still be counted
        queue = collections.deque()
        for string in strs:
            if string not in visited:
                queue.append(string)
                visited.add(string)
                while queue:
                    cur_str = queue.popleft()
                    for neighbor in connected[cur_str]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
                ans+=1        
        return ans
    
    def is_similar(self, str1, str2):
        if str1 == str2:
            return True
        n = len(str1)
        diff = 0
        for i in range(n):
            if str1[i] != str2[i]:
                diff+=1
            if diff > 2:
                return False
        return True
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**

****

## Solution - DFS

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        start = strs[0]
        connected  = collections.defaultdict(set)
        for i in range(len(strs) - 1):
            for j in range(1, len(strs)):
                if self.is_similar(strs[i], strs[j]):
                    connected[strs[i]].add(strs[j])
                    connected[strs[j]].add(strs[i])
        visited = set()
        ans = 0
       
        # because we are traversing all the string in strs, so those not belongs to connected groups
        # will still be counted
        for string in strs:
            if string not in visited:
                self.dfs(string, connected, visited)
                ans+=1        
        return ans
    
    def is_similar(self, str1, str2):
        if str1 == str2:
            return True
        n = len(str1)
        diff = 0
        for i in range(n):
            if str1[i] != str2[i]:
                diff+=1
            if diff > 2:
                return False
        return True

    def dfs(self, string, connected, visited):
        visited.add(string)
        for neighbor in connected[string]:
            if neighbor not in visited:
                self.dfs(neighbor, connected, visited)

```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
