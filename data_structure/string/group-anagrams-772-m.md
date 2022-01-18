# Group Anagrams 772 (M)

## Problem

To give you a string array, please group the misplaced words(refers to the same character string with different permutations).

All inputs will be in lower-case.Example

Example 1:

```
Input:
["eat","tea","tan","ate","nat","bat"]
Output:
[["ate","eat","tea"],
 ["bat"],
 ["nat","tan"]]
```

Example 2:

```
Input:
["eat","nowhere"]
Output:
[["eat"],
 ["nowhere"]]
```

## Solution - Categroized by sorted strings

### Code

{% tabs %}
{% tab title="python" %}
```python
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rec = collections.defaultdict(list)
        
        for s in strs:
            sort_s = "".join(sorted(s))
            rec[sort_s].append(s)
            
        return rec.values()
```
{% endtab %}

{% tab title="java" %}
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0)
            return new ArrayList();
        
        Map<String, List> ans = new HashMap<String, List>();
        for (String s : strs) {
            char[] ch_arr = s.toCharArray();
            Arrays.sort(ch_arr);
            String key = new String(ch_arr);
            if (!ans.containsKey(key))
                ans.put(key, new ArrayList());
            ans.get(key).add(s);
        }
        return new ArrayList(ans.values());
    }
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nklogk)**
  * n: length of strs
  * k: maximum length of string in strs
* **Space Complexity: O(nk)**

## Solution - Categorized by counts

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        # write your code here
        # ans = collections.defaultdict(list)
        ans = {}
        for s in strs: #O(n)
            count = [0] * 26
            for c in s: #O(k)
                count[ord(c) - ord('a')]+=1
            # since list is unhashable 
            if tuple(count) not in ans:
                ans[tuple(count)] = [s]
            else:
                ans[tuple(count)].append(s)
        return ans.values()
```
{% endtab %}

{% tab title="java" %}
```
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(nk)**
  * n: length of strs
  * k: maximum length of string in strs
* **Space Complexity: O(nk)**
