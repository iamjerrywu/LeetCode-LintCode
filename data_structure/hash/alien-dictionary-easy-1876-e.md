# Alien Dictionary(easy) 1876 (E)

## Problem

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.\
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.Otherwise, it returns false.

1. 1 <= words.length <= 100
2. 1 <= words\[i].length <= 20
3. order.length == 26
4. All characters in words\[i] and order are English lowercase letters.

Example

**Example 1:**

```
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"Output: trueExplanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
```

**Example 2:**

```
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"Output: falseExplanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
```

**Example 3:**

```
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"Output: falseExplanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
```

## Solution&#x20;

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param words: the array of string means the list of words
    @param order: a string indicate the order of letters
    @return: return true or false
    """
    def isAlienSorted(self, words, order):
        # write your code here.
        alien_dict = {}
        for i in range(len(order)):
            alien_dict[order[i]] = i
        
        for i in range(1, len(words)):
            if not self.is_valid(words[i - 1], words[i], alien_dict):
                return False
        return True
    
    def is_valid(self, word1, word2, alien_dict):
        for i in range(min(len(word1), len(word2))):
            if alien_dict[word1[i]] < alien_dict[word2[i]]:
                return True
            elif alien_dict[word1[i]] > alien_dict[word2[i]]:
                return False
            #else:
                # do nothing
        return len(word1) <= len(word2)
```
{% endtab %}

{% tab title="Python (Better)" %}
```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = [0] * 26
        for i in range(len(order)):
            order_map[ord(order[i]) - ord('a')] = i
        for i in range(len(words) - 1):
            if not self.is_order(words[i], words[i + 1], order_map):
                return False
        return True
    
    def is_order(self, word1, word2, order_map):
        pt1, pt2 = 0, 0
        
        while pt1 < len(word1) and pt2 < len(word2):
            if order_map[ord(word1[pt1]) - ord('a')] > order_map[ord(word2[pt2]) - ord('a')]:
                return False
            elif order_map[ord(word1[pt1]) - ord('a')] < order_map[ord(word2[pt2]) - ord('a')]:
                return True
            else:
                pt1+=1
                pt2+=1
        return len(word1) <= len(word2)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O(n)**
* **Space Complexity: O(1)**
