# First Unique Character in a String 209 (E)

## Problem

Given a string and find the first unique character in a given string. You can assume that there is at least one unique character in the string.Example

```
Example 1:
	Input: "abaccdeff"
	Output:  'b'
	
	Explanation:
	There is only one 'b' and it is the first one.


Example 2:
	Input: "aabccd"
	Output:  'b'
	
	Explanation:
	'b' is the first one.
```

## Solution&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        ref = {}
        for c in str:
            ref[c] = ref.get(c, 0) + 1
        
        for k in ref:
            if ref[k] == 1:
                return k
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    int firstUniqChar(string s) {
        int arr[26] = {0};
        for (char c : s) {
            arr[c - 'a']+=1;
        }

        for (int i = 0; i < s.length(); i++) {
            if (arr[s[i] - 'a'] == 1) return i; 
        }
        return -1;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**



#### Follow-up

If support up to ASCII (256 Characters), we can literally cast to unsigned char&#x20;

```c++
// Cast to unsigned char to safely handle potential negative char values
 arr[static_cast<unsigned char>(c)] += 1; 
```

If support up to full unicode, can just use unordered\_map

```cpp
std::unordered_map<char, int> count_map; 
```
