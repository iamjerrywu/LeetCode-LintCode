# Group Shifted Strings (LeetCode 249) (M)

## Problem



We can shift a string by shifting each of its letters to its successive letter.

* For example, `"abc"` can be shifted to be `"bcd"`.

We can keep shifting the string to form a sequence.

* For example, we can keep shifting `"abc"` to form the sequence: `"abc" -> "bcd" -> ... -> "xyz"`.

Given an array of strings `strings`, group all `strings[i]` that belong to the same shifting sequence. You may return the answer in **any order**.

&#x20;

**Example 1:**

```
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
```

**Example 2:**

```
Input: strings = ["a"]
Output: [["a"]]
```

&#x20;

**Constraints:**

* `1 <= strings.length <= 200`
* `1 <= strings[i].length <= 50`
* `strings[i]` consists of lowercase English letters.



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        rec = collections.defaultdict(list)
        
        for string in strings:
            
            key = ""
            for i in range(len(string) - 1):
                # to make the wrap difference the same, adding 26 then modulo 26
                # i.e:
                # az -> ord(z) - ord(a) = 26 - 1 = 25, (25 + 26)%26 = 25
                # ba -> ord(a) - ord(b) = 1 - 2 = -1,  (-1 + 26)%26 = 25
                
                key+=str(((ord(string[i + 1]) - ord(string[i])) + 26)%26)
                # add '.' to avoid coner case like "abc", "al", which both have the same different as "11"
                # now, adding '.' can make them different as "1.1." vs "11."
                key+='.'
            rec[key].append(string)
        return rec.values()
        
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

* **Time Complexity: O(n \* m)**
* **Space Complexity:**

