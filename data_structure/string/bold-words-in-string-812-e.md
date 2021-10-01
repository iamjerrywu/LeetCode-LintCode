# Bold Words in String 812 \(E\)

## Problem

{% hint style="danger" %}
This problem is a fake easy, more like a medium + 
{% endhint %}

Description

Given a set of keywords `words` and a string `S`, make all appearances of all keywords in S bold. Any letters between `<b>` and `</b>` tags become bold.  
The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

* `words` has length in range `[0, 50]`.
* `words[i]` has length in range `[1, 10]`.
* `S` has length in range `[0, 500]`.
* All characters in `words[i]` and `S` are lowercase letters.

Example

**Example 1:**

```text
Input:
["ab", "bc"]
"aabcd"
Output:
"a<b>abc</b>d"

Explanation:
Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.
```

**Example 2:**

```text
Input:
["bcccaeb","b","eedcbda","aeebebebd","ccd","eabbbdcde","deaaea","aea","accebbb","d"]
"ceaaabbbedabbecbcced"
Output:
"ceaaa<b>bbb</b>e<b>d</b>a<b>bb</b>ec<b>b</b>cce<b>d</b>"
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param words: the words
    @param S: the string
    @return: the string with least number of tags
    """
    def boldWords(self, words, S):
        # Write your code here
        n = len(S)
        bold = [0] * n
        # bold list same length as S, and mark those need to bold as 1 (0 if not need)
        for word in words:
            start = 0
            while True:
                # need to keep find since there might be multiple word in S
                idx = S[start:].find(word)
                if idx < 0:
                    break
                for j in range(start + idx, start + idx + len(word)):
                    bold[j] = 1
                start+=idx + 1
        
        ans = []
        for i in range(0, n):
            #1...
            if i == 0 and bold[i] == 1:
                ans.append('<b>')
            #..01..
            elif i > 0 and bold[i - 1] == 0 and bold[i] == 1:
                ans.append('<b>')
            ans.append(S[i])
            #..10..
            if i < n - 1 and bold[i] == 1 and bold[i + 1] == 0:
                ans.append('</b>')
            #..1
            elif i == n - 1 and bold[i] == 1:
                ans.append('</b>')
        return ''.join(ans) 
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

