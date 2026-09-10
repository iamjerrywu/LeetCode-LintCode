# Reverse Words in a String 53 (E)

## Problem

Given an input string, reverse the string word by word.

* What constitutes a word?\
  A sequence of non-space characters constitutes a word and some words have punctuation at the end.
* Could the input string contain leading or trailing spaces?\
  Yes. However, your reversed string should not contain leading or trailing spaces.
* How about multiple spaces between two words?\
  Reduce them to a single space in the reversed string.

Example

**Example 1:**

Input:

```
s = "the sky is blue"
```

Output:

```
"blue is sky the"
```

Explanation:

return a reverse the string word by word.\
**Example 2:**

Input:

```
s = "hello world"
```

Output:

```
"world hello"
```

Explanation:

return a reverse the string word by word.

## Solution - Copy String

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        if not s:
            return s

        str_list = s.split()
        ans = " "
        return ans.join(str_list[::-1])
        
```
{% endtab %}

{% tab title="C++" %}


```cpp
class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        vector<string> words;
        string word;
        
        // this help you to generate the word and handle the spaces
        while(ss >> word) {
            words.push_back(word);
        }
        string ans;
        for (int i = words.size() - 1; i >= 0; i--) {
            ans+=words[i];
            if (i > 0) ans+=" ";
        }
        return ans;
                
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(n)**<br>

## Solution - In-place&#x20;

### Code

{% tabs %}
{% tab title="python" %}
```python
```
{% endtab %}

{% tab title="C++" %}


```cpp
class Solution {
public:
    string reverseWords(string s) {
        // we first reverse entire string
        reverse(s.begin(), s.end());
        
        int writeIdx = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != ' ') {
                if (writeIdx != 0) {
                    s[writeIdx++] = ' ';
                }
                // then we find each word, and reverse them
                int start = writeIdx;
                while (s[i] != ' ' && i < s.length()) {
                    s[writeIdx++] = s[i++];
                }
                
                reverse(s.begin() + start, s.begin() + writeIdx);
            }
        }

        /* we don't write return s.substr(0, writeIdx);, 
        because that will force to allocate a brand-new block of memory [1] elsewhere, 
        copy the characters from s into that new memory, and return it
        */
        s.resize(writeIdx);
        return s;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**<br>
