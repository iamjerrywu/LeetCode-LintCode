# Word Break III 683 \(M\)

## Problem

Description

Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.

Ignore caseExample

**Example1**

```text
Input:
"CatMat"
["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
Output: 3
Explanation:
we can form 3 sentences, as follows:
"CatMat" = "Cat" + "Mat"
"CatMat" = "Ca" + "tM" + "at"
"CatMat" = "C" + "at" + "Mat"
```

**Example1**

```text
Input:
"a"
[]
Output: 
0
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        # Write your code here
        
        # Since cases unsensitive, transform to lower cases
        s = s.lower()
        dict = set([word.lower() for word in dict])
        # dp[i]: the numbers of how many sentences can be divided in the first ith characters
        dp = [0] * (len(s) + 1)
        # need to init dp[0] as 1 
        dp[0] = 1
        
        # if s[i - j : i] in dict, then dp[i] = dp[i] + dp[i - j]
        for i in range(1, len(s) + 1):
            for j in range(1, len(s) + 1):
                if s[i - j : i] in dict:
                    dp[i]+=dp[i - j]
        return dp[-1]

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

