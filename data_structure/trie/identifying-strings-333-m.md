# Identifying Strings 333 \(M\)

## Problem

Given n character strings containing only lower case letters, find the minimum prefix strings that can identify each string.  
That is, the minimum prefix string Ap which identifies string A will not be a prefix string of other n-1 character strings.

1 &lt;= n &lt;= 500  
The length of strings would not exceed 100.  
If string S is a profix of string T, the answer of S will be itself.Example

Input:\["aaa","bbc","bcd"\]  
Output:\["a","bb","bc"\]  
Explanation:"a" is only the profix of "aaa".  
"bb" is only the profix of "bbc".  
"bc" is only the profix of "bcd".

## Solution - Brute Force Enumeration

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param stringArray: a string array
    @return: return every strings'short peifix
    """
    def ShortPerfix(self, stringArray):
        # write your code here
        prefix_sum_cnt = self.get_prefix_sum_cnt(stringArray)
        res = []
        for string in stringArray:
            cur_string = ''
            for i in range(len(string)):
                cur_string = string[:i + 1]
                if prefix_sum_cnt[cur_string] == 1 or i == len(string) - 1:
                    res.append(cur_string)
                    break
        return res
    
    def get_prefix_sum_cnt(self, stringArray):
        prefix_sum_cnt = {}
        for string in stringArray:
            cur_string = ''
            for i in range(len(string)):
                cur_string = string[:i + 1]
                prefix_sum_cnt[cur_string] = prefix_sum_cnt.get(cur_string, 0) + 1
        return prefix_sum_cnt
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

