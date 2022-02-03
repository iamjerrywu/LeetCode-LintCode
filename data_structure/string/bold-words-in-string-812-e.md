# Bold Words in String 812 (E)

## Problem

{% hint style="danger" %}
This problem is a fake easy, more like a medium +&#x20;
{% endhint %}

Description

Given a set of keywords `words` and a string `S`, make all appearances of all keywords in S bold. Any letters between `<b>` and `</b>` tags become bold.\
The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

* `words` has length in range `[0, 50]`.
* `words[i]` has length in range `[1, 10]`.
* `S` has length in range `[0, 500]`.
* All characters in `words[i]` and `S` are lowercase letters.

Example

**Example 1:**

```
Input:
["ab", "bc"]
"aabcd"
Output:
"a<b>abc</b>d"

Explanation:
Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.
```

**Example 2:**

```
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
import collections
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        rec = collections.defaultdict(list)
        
        for word in words:
            self.process(s, word, rec)
        rec_list = []
        
        for v_list in rec.values():
            for start, end in v_list:
                rec_list.append([start, end])
        
        rec_list.sort(key = lambda r:(r[0], r[1]))
        new_rec_list = []
        
        for start, end in rec_list:
            
            if not new_rec_list or new_rec_list[-1][1] + 1 < start:
                new_rec_list.append([start, end])
            else:
                new_rec_list[-1][1] = max(new_rec_list[-1][1], end)
        
        ans = self.generate_ans(s, new_rec_list)
        return ans
    
    def process(self, s, word, rec):
        start = 0
        offset = 0
        while s.find(word) != -1:
            start = s.find(word)
            
            rec[word].append([offset + start, offset + start + len(word) - 1])
            offset+= start + 1
            s = s[start + 1:]
                
    def generate_ans(self, s, new_rec_list):
        ans = ""
        idx = 0
        for i in range(len(s)):
            if idx < len(new_rec_list) and i == new_rec_list[idx][0]:
                ans+="<b>"
                ans+=s[i]
                if i == new_rec_list[idx][1]:
                    ans+="</b>"
                    idx+=1
            elif idx < len(new_rec_list) and i == new_rec_list[idx][1]:
                ans+=s[i]
                ans+="</b>"
                idx+=1
            else:
                ans+=s[i]
        return ans
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

{% tab title="Python (Better)" %}
```python
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        flag = [0] * len(s)
        cur_end = -1
        for i in range(len(s)):
            for word in words:
                if s.startswith(word, i):
                # if s[i:].find(word) == 0:
                    cur_end = max(cur_end, i + len(word) - 1)
            flag[i] = i <= cur_end
        
        ans = ""
        for i in range(len(flag)):
            if flag[i] and (i == 0 or not flag[i - 1]):
                ans+="<b>"
            ans+=s[i]
            if flag[i] and (i == len(s) - 1 or not flag[i + 1]):
                ans+="</b>"
            
        return ans
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
