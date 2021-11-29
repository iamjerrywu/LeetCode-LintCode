# Design Add and Search Words Data Structure (LeetCode 211) (M)

## Problem

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

* `WordDictionary()` Initializes the object.
* `void addWord(word)` Adds `word` to the data structure, it can be matched later.
* `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

&#x20;

**Example:**

```
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

&#x20;

**Constraints:**

* `1 <= word.length <= 500`
* `word` in `addWord` consists lower-case English letters.
* `word` in `search` consist of  `'.'` or lower-case English letters.
* At most `50000` calls will be made to `addWord` and `search`.

## Solution

{% tabs %}
{% tab title="Python" %}
```python
class WordDictionary:

    def __init__(self):
        self.dict = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        self.dict[len(word)].add(word)

    def search(self, word: str) -> bool:
        n = len(word)
        for dict_word in self.dict[n]:
            i = 0
            while i < n and (dict_word[i] == word[i] or word[i] == '.'):
                i+=1
            if i == n:
                return True
        return False
                             
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
