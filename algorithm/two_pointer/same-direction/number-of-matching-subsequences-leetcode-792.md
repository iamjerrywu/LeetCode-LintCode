# Number of Matching Subsequences (LeetCode 792)

### Problem <a href="#problem" id="problem"></a>

​​

Given a string `s` and an array of strings `words`, return _the number of_ `words[i]` _that is a subsequence of_ `s`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

* For example, `"ace"` is a subsequence of `"abcde"`.

&#x20;

**Example 1:**

<pre><code><strong>Input: s = "abcde", words = ["a","bb","acd","ace"]
</strong><strong>Output: 3
</strong><strong>Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
</strong><strong>Output: 2
</strong></code></pre>

&#x20;

**Constraints:**

* `1 <= s.length <= 5 * 10`<sup>`4`</sup>
* `1 <= words.length <= 5000`
* `1 <= words[i].length <= 50`
* `s` and `words[i]` consist of only lowercase English letters.

### Solution <a href="#solution" id="solution"></a>

So we first create the vector, that stores each char of s's appearing idx, then we use binary search to find each char in word, with that vector, is it's always in order, then means it's a subsequence.

## Solution - Binary Search + vector

{% tabs %}
{% tab title="C++" %}
```cpp
class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        vector<vector<int>> sIndices(26);
        for (int i = 0; i < s.length(); i++) {
            sIndices[s[i] - 'a'].push_back(i);
        }
        int ans = 0;
        for (string &word : words) {
            int prevIdx = -1;
            bool isSubseq = true;
            for (int i = 0; i < word.length(); i++) {

                // using binary search here
                int findIdx = search(sIndices[word[i] - 'a'], prevIdx + 1);
                if (findIdx == -1)  {
                    isSubseq = false;   
                    break;
                }
                prevIdx = sIndices[word[i] - 'a'][findIdx];
            }
            if (isSubseq) ans+=1;
        }
        return ans;
    }
private:
    int search(vector<int> &indices, int target) {
        if (indices.empty()) return -1;

        int start = 0, end = indices.size() - 1;
        while (start + 1 < end) {
            int mid = start + (end - start)/2;
            if (indices[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }
        if (indices[start] >= target) return start;
        if (indices[end] >= target) return end;
        return -1;
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity: O(len(s) +** $$\sum_{\text{word} \in W} |\text{word}| \cdot \log(|s|)$$
* **Space Complexity: O(len(s))**
