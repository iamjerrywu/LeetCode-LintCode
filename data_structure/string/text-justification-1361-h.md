# Text Justification 1361 \(H\)

## Problem

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully \(left and right\) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no **extra** space is inserted between words.

· A word is defined as a character sequence consisting of non-space characters only.  
· Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.  
· The input array `words` contains at least one word.Example

**Example 1:**

```text
Input:words = ["This", "is", "an", "example", "of", "text", "justification."]maxWidth = 16Output:[   "This    is    an",   "example  of text",   "justification.  "]
```

**Example 2:**

```text
Input:words = ["What","must","be","acknowledgment","shall","be"]maxWidth = 16Output:[  "What   must   be",  "acknowledgment  ",  "shall be        "]Explanation: Note that the last line is "shall be    " instead of "shall     be",             because the last line must be left-justified instead of fully-justified.             Note that the second line is also left-justified becase it contains only one word.
```

**Example 3:**

```text
Input:words = ["Science","is","what","we","understand","well","enough","to","explain",         "to","a","computer.","Art","is","everything","else","we","do"]maxWidth = 20Output:[  "Science  is  what we",  "understand      well",  "enough to explain to",  "a  computer.  Art is",  "everything  else  we",  "do                  "]
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # write your code here
        res = []
        if len(words) == 1:
            res.append(self.format(words, maxWidth, False))
            return res
        idx, len_cnt =0, 0
        str_arr = []
        while idx < len(words):
            len_cnt+=len(words[idx])
            if len_cnt > maxWidth:
                res.append(self.format(str_arr, maxWidth, False))
                len_cnt = 0
                str_arr = []
                continue
            str_arr.append(words[idx])
            idx+=1
            len_cnt+=1
        res.append(self.format(str_arr, maxWidth, True))
        return res
    
    def format(self, str_arr, maxWidth, end):
        n = len(str_arr)
        ch_len = sum([len(w) for w in str_arr])
        space_len = maxWidth - ch_len
        str_ans = ''
        if n == 1:
            return str_arr[0] + space_len * ' '
        if n > 1:
            idx, space_cnt =0, 0
            if end is True:
                space_list = [0] * n
                for i in range(len(space_list)):
                    space_list[i]+=1
                    space_len-=1
                space_list[-1]+=space_len
                for i in range(n):
                    str_ans+=str_arr[i]
                    str_ans+=space_list[i] * ' '
            else:
                space_list = [0] * (n - 1)
                while space_cnt < space_len:
                    space_list[idx%(n - 1)]+=1
                    space_cnt+=1
                    idx+=1
                for i in range(n):
                    str_ans+=str_arr[i]
                    if i != n - 1:
                        str_ans+=space_list[i] * ' '
        return str_ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n \* L\) or O\(sum\(words\)\)**
  * n: len\(words\)
  * L: len\(word\) for word in words
* **Space Complexity:**

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

