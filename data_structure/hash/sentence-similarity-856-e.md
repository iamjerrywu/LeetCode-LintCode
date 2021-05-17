# Sentence Similarity 856 \(E\)

## Problem



Given two sentences `words1`, `words2` \(each represented as an array of strings\), and a list of similar word pairs `pairs`, determine if two sentences are similar.

For example, `words1 = great acting skills` and `words2 = fine drama talent` are similar, if the similar word pairs are `pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]]`.

Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are **not** necessarily similar.

However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences `words1 = ["great"], words2 = ["great"], pairs = []` are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like `words1 = ["great"]` can never be similar to `words2 = ["doubleplus","good"]`.

1.The length of words1 and words2 will not exceed 1000.  
2.The length of pairs will not exceed 2000.  
3.The length of each pairs\[i\] will be 2.  
4.The length of each words\[i\] and pairs\[i\]\[j\] will be in the range \[1, 20\].Example

**Example1**

```text
Input: words1 = ["great","acting","skills"], words2 = ["fine","drama","talent"] and pairs = [["great","fine"],["drama","acting"],["skills","talent"]]
Output: true
Explanation:
"great" is similar with "fine"
"acting" is similar with "drama"
"skills" is similar with "talent"
```

**Example2**

```text
Input: words1 = ["fine","skills","acting"], words2 = ["fine","drama","talent"] and pairs = [["great","fine"],["drama","acting"],["skills","talent"]]
Output: false
Explanation:
"fine" is the same as "fine"
"skills" is not similar with "drama"
"acting" is not similar with "talent"
```

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

