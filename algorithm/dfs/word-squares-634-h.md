# Word Squares 634 \(H\)

## Problem

Given a set of words **without duplicates**, find all [`word squares`](https://en.wikipedia.org/wiki/Word_square) you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k &lt; max\(numRows, numColumns\).

For example, the word sequence `["ball","area","lead","lady"]` forms a word square because each word reads the same both horizontally and vertically.

```text
b a l la r e al e a dl a d y
```

* There are at least 1 and at most 1000 words.
* All words will have the exact same length.
* Word length is at least 1 and at most 5.
* Each word contains only lowercase English alphabet `a-z`.

Example

**Example 1:**

```text
Input:["area","lead","wall","lady","ball"]Output:[["wall","area","lead","lady"],["ball","area","lead","lady"]]Explanation:The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
```

**Example 2:**

```text
Input:["abat","baba","atan","atal"]Output: [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
```

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        # write your code here
        prefix_to_words = self.get_prefix_to_words(words)
        print(prefix_to_words)

        squares = []
        # first ensure the first row of word
        for word in words:
            self.search(prefix_to_words, [word], squares)
        
        return squares
    
    def search(self, prefix_to_words, square, squares):
        cur_id = len(square)
        if cur_id == len(square[0]):
            squares.append(list(square))
            return 

        # then based on the first row of word
        # find the latter columns index words that should put with the prefix that's column index[0 ~ cur_id]
        prefix = ''.join([square[i][cur_id] for i in range(cur_id)])
        print(prefix)
        for word in prefix_to_words.get(prefix, []):
            square.append(word)
            self.search(prefix_to_words, square, squares)
            square.pop()
    
    def get_prefix_to_words(self, words):
        prefix_to_words = {}
        for word in words:
            for i in range(len(word)):
                prefix = word[:i + 1]
                if prefix not in prefix_to_words:
                    prefix_to_words[prefix] = []
                prefix_to_words[prefix].append(word)
        return prefix_to_words

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

