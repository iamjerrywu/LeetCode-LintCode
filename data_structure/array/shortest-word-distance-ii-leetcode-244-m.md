# Shortest Word Distance II \(LeetCode 244\) \(M\)

## Problem

Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

Implement the `WordDistance` class:

* `WordDistance(String[] wordsDict)` initializes the object with the strings array `wordsDict`.
* `int shortest(String word1, String word2)` returns the shortest distance between `word1` and `word2` in the array `wordsDict`.

**Example 1:**

```text
Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1
```

**Constraints:**

* `1 <= wordsDict.length <= 3 * 104`
* `1 <= wordsDict[i].length <= 10`
* `wordsDict[i]` consists of lowercase English letters.
* `word1` and `word2` are in `wordsDict`.
* `word1 != word2`
* At most `5000` calls will be made to `shortest`.

## Solution - HashSet + Sort

{% tabs %}
{% tab title="Python" %}
```python
import collections
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.appear = collections.defaultdict(list)
        for i in range(len(wordsDict)):
            self.appear[wordsDict[i]].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        pos = []
        for v in self.appear[word1]:
            pos.append([1, v])
        for v in self.appear[word2]:
            pos.append([2, v])
        pos = self.merge(self.appear[word1], self.appear[word2])
        
        # can use sort here, but will take O(nlogn) time
        # pos.sort(key = lambda p:p[1])
        ans = float('inf')
        
        for i in range(len(pos) - 1):
            if pos[i][0] != pos[i + 1][0]:
                ans = min(ans, pos[i + 1][1] - pos[i][1])
        return ans
    
    def merge(self, arr1, arr2):
        length = len(arr1) + len(arr2)
        ans = []
        
        pt1, pt2 = 0, 0
        for i in range(length):
            if pt1 < len(arr1) and (pt2 >= len(arr2) or arr1[pt1] < arr2[pt2]):
                ans.append([1, arr1[pt1]])
                pt1+=1
            else:
                ans.append([2, arr2[pt2]])
                pt2+=1
        return ans
        
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
```
{% endtab %}
{% endtabs %}

* **Time Complexity:** 
  * Shortest: O\(n\)
    * n: len\(word1\) + len\(word2\)
* **Space Complexity: O\(n\)**

