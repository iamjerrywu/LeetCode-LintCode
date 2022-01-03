# Zigzag Conversion (LeetCode 6) (M)

## Problem



The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

&#x20;

**Example 1:**

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

**Example 2:**

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

**Example 3:**

```
Input: s = "A", numRows = 1
Output: "A"
```

&#x20;

**Constraints:**

* `1 <= s.length <= 1000`
* `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.
* `1 <= numRows <= 1000`



## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        arr = [[] for _ in range(numRows)]
        
        # init as -1, since we change to 1 later in the beginning
        direction = -1 
        index = 0
        for c in s:
            if index == 0 or index == numRows - 1:
                direction*=-1
            
            arr[index].append(c)
            index+=direction
        
        ans = ""
        for str_list in arr:
            ans+=''.join(str_list)
        return ans
```
{% endtab %}

{% tab title="Java" %}
```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        
        vector<string> rows(min(numRows, int(s.size())));
        
        int idx = 0;
        int inc = -1;
        
        for (int i = 0; i < s.size(); i++) {
            if (i%(numRows - 1) == 0) {
                inc*=-1;
            }
            rows[idx]+=s[i];
            idx+=inc;
        }
        string res;
        for (string row : rows) res+=row;
        return res;    
    }
};
```
{% endtab %}

{% tab title="C++" %}

{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**
