# Expressive Words 1008 \(M\)

## Problem

Sometimes people repeat letters to represent extra feeling. For example:

* `"hello" -> "heeellooo"`
* `"hi" -> "hiiii"`

In these strings like `"heeellooo"`, we have groups of adjacent letters that are all the same: `"h"`, `"eee"`, `"ll"`, `"ooo"`.

You are given a string `s` and an array of query strings `words`. A query word is **stretchy** if it can be made to be equal to `s` by any number of applications of the following extension operation: choose a group consisting of characters `c`, and add some number of characters `c` to the group so that the size of the group is **three or more**.

* For example, starting with `"hello"`, we could do an extension on the group `"o"` to get `"hellooo"`, but we cannot get `"helloo"` since the group `"oo"` has a size less than three. Also, we could do another extension like `"ll" -> "lllll"` to get `"helllllooo"`. If `s = "helllllooo"`, then the query word `"hello"` would be **stretchy** because of these two extension operations: `query = "hello" -> "hellooo" -> "helllllooo" = s`.

Return _the number of query strings that are **stretchy**_.

**Example 1:**

```text
Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
```

**Example 2:**

```text
Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3
```

**Constraints:**

* `1 <= s.length, words.length <= 100`
* `1 <= words[i].length <= 100`
* `s` and `words[i]` consist of lowercase letters.

## Solution 

Update the two pointers and also count their appearances until the next character is not the same.

Then go check the requirements as follows:

1. If a letter is not repeated in a word in the **words** list, the stretched word must contain either one such letter, or three or more such letters, but not two such letters.
2. If a letter is repeated once \(two same consecutive letters\), the stretched word must contain two or more such letters.

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param S: a string
    @param words: a list of strings
    @return: return a integer
    """
    def expressiveWords(self, S, words):
        # write your code here
        cnt = 0
        for word in words:
            if self.is_stretchy(S, word):
                cnt+=1
        return cnt
    
    def is_stretchy(self, S, word):
        S_p, word_p = 0, 0
        S_cnt, word_cnt = 1, 1
        while S_p < len(S) and word_p < len(word):
            while S_p < len(S) - 1 and S[S_p] == S[S_p + 1]:
                S_p+=1
                S_cnt+=1
            while word_p < len(word) - 1 and word[word_p] == word[word_p + 1]:
                word_p+=1
                word_cnt+=1

            # if not the same, return False
            if S[S_p] != word[word_p]:
                return False
            # two cases is valid:
            #If a letter is not repeated in a word in the words list, the stretched word must contain either one such letter, or three or more such letters, but not two such letters.
            #If a letter is repeated once (two same consecutive letters), the stretched word must contain two or more such letters.
            if (word_cnt == 1 and (S_cnt == 1 or S_cnt >= word_cnt * 3)) or (word_cnt > 1 and S_cnt >= word_cnt):
                S_p+=1
                word_p+=1
                S_cnt = 1
                word_cnt = 1
            else:
                return False
        return True

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n\)**
* **Space Complexity: O\(1\)**

