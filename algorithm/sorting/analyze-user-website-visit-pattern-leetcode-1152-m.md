# Analyze User Website Visit Pattern (LeetCode 1152) (M)

## Problem



You are given two string arrays `username` and `website` and an integer array `timestamp`. All the given arrays are of the same length and the tuple `[username[i], website[i], timestamp[i]]` indicates that the user `username[i]` visited the website `website[i]` at time `timestamp[i]`.

A **pattern** is a list of three websites (not necessarily distinct).

* For example, `["home", "away", "love"]`, `["leetcode", "love", "leetcode"]`, and `["luffy", "luffy", "luffy"]` are all patterns.

The **score** of a **pattern** is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

* For example, if the pattern is `["home", "away", "love"]`, the score is the number of users `x` such that `x` visited `"home"` then visited `"away"` and visited `"love"` after that.
* Similarly, if the pattern is `["leetcode", "love", "leetcode"]`, the score is the number of users `x` such that `x` visited `"leetcode"` then visited `"love"` and visited `"leetcode"` **one more time** after that.
* Also, if the pattern is `["luffy", "luffy", "luffy"]`, the score is the number of users `x` such that `x` visited `"luffy"` three different times at different timestamps.

Return _the **pattern** with the largest **score**_. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.

**Example 1:**

```
Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: The tuples in this example are:
["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
The pattern ("home", "about", "career") has score 2 (joe and mary).
The pattern ("home", "cart", "maps") has score 1 (james).
The pattern ("home", "cart", "home") has score 1 (james).
The pattern ("home", "maps", "home") has score 1 (james).
The pattern ("cart", "maps", "home") has score 1 (james).
The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).
```

**Example 2:**

```
Input: username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]
Output: ["a","b","a"]
```

**Constraints:**

* `3 <= username.length <= 50`
* `1 <= username[i].length <= 10`
* `timestamp.length == username.length`
* `1 <= timestamp[i] <= 109`
* `website.length == username.length`
* `1 <= website[i].length <= 10`
* `username[i]` and `website[i]` consist of lowercase English letters.
* It is guaranteed that there is at least one user who visited at least three websites.
* All the tuples `[username[i], timestamp[i], website[i]]` are **unique**.

## Solution

{% tabs %}
{% tab title="Python" %}
```python
import collections
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(username)
        
        user_rec = collections.defaultdict(list)
        domain_rec = collections.defaultdict(int)
        rec = []
        for i in range(n):
            rec.append([username[i], timestamp[i], website[i]])
        
        rec.sort(key = lambda e:e[1])
        for i in range(n):
            user_rec[rec[i][0]].append(rec[i][2])
        for k, v_list in user_rec.items():
            if len(v_list) >= 3:
                self.update(domain_rec, v_list)
        k_v_list = [[k, v] for k, v in domain_rec.items()]
        k_v_list.sort(key = lambda e:(-e[1], e[0]))
        return k_v_list[0][0]
    
    # pick every three distinct item from the arr (orders matters)
    def update(self, domain_rec, arr):
        visited = set()
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if (arr[i], arr[j], arr[k]) not in visited:
                        visited.add((arr[i], arr[j], arr[k]))
                        domain_rec[(arr[i], arr[j], arr[k])]+=1
```
{% endtab %}

{% tab title="C++" %}
```cpp
class Solution {
public:
    vector<string> mostVisitedPattern(vector<string>& username, vector<int>& timestamp, vector<string>& website) {
        unordered_map<string, map<int, string>> records;
        unordered_map<string, int> freq;
        
        for (int i = 0; i < username.size(); i++) {
            records[username[i]][timestamp[i]] = website[i];
        }
        
        for (auto kv1 : records) {
            vector<string> webRec;
            for (auto kv2 : kv1.second) {
                webRec.push_back(kv2.second);
            }

            // every three is pattern
            if (webRec.size() >= 3) {
                update(webRec, freq);
            }
        }
           
        string maxPattern = "";
        int maxCnt = 0;
        
        for (auto kv : freq) {
            if (kv.second == maxCnt) {
                maxPattern = min(maxPattern, kv.first);
            } else if (kv.second > maxCnt) {
                maxPattern = kv.first;
                maxCnt = kv.second;
            }
        }
        int firstSpace = maxPattern.find(" ");
        int secondSpace = maxPattern.substr(firstSpace + 1).find(" ");
        return {maxPattern.substr(0, firstSpace), maxPattern.substr(firstSpace + 1, secondSpace), maxPattern.substr(firstSpace + 1).substr(secondSpace + 1)};
    }

private:
    void update(vector<string> &webRec, unordered_map<string, int> &freq) {
        // need to ensure for one user, the pattern can only be count once
        set<string> visited;
        for (int i = 0; i < webRec.size(); i++) 
            for (int j = i + 1; j < webRec.size(); j ++) 
                for (int k = j + 1; k < webRec.size(); k++) {
                    string key = webRec[i] +" " + webRec[j] + " " + webRec[k];
                    if (visited.count(key) == 0) {
                        visited.insert(key);
                        if (freq.count(key) == 0) freq[key] = 1;
                        else freq[key]+=1;
                    }
                }
    }
};
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**&#x20;
* **Space Complexity:**
