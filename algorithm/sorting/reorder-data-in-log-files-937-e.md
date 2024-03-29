# Reorder Data in Log Files 937 (E)

## Problem

You are given an array of `logs`. Each log is a space-delimited string of words, where the first word is the **identifier**.

There are two types of logs:

* **Letter-logs**: All words (except the identifier) consist of lowercase English letters.
* **Digit-logs**: All words (except the identifier) consist of digits.

Reorder these logs so that:

1. The **letter-logs** come before all **digit-logs**.
2. The **letter-logs** are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
3. The **digit-logs** maintain their relative ordering.

Return _the final order of the logs_.

**Example 1:**

```
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
```

**Example 2:**

```
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
```

**Constraints:**

* `1 <= logs.length <= 100`
* `3 <= logs[i].length <= 100`
* All the tokens of `logs[i]` are separated by a **single** space.
* `logs[i]` is guaranteed to have an identifier and at least one word after the identifier.



## Solution - Lambda Sorting (Straight)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []
        
        for log in logs:
            if log.split()[1].isalpha():
                letter.append(log)
            else:
                digit.append(log)
        # i.e: l = "a1 do what cat"
        # split(' ', 1)[1] = "do what cat"
        # split(' ', 1)[0] = 'a1'
        return sorted(letter, key = lambda l:(l.split(' ', 1)[1], l.split(' ', 1)[0])) + digit
        
```
{% endtab %}

{% tab title="c++" %}
```cpp
class Solution {
public:
    static bool compare(string str1, string str2) {
        // sort by contents
        string str1Contents = str1.substr(str1.find(' '));
        string str2Contents = str2.substr(str2.find(' '));
        
        return str1Contents == str2Contents ? str1 < str2 : str1Contents < str2Contents;
    }
    vector<string> reorderLogFiles(vector<string>& logs) {
        vector<string> result;
        int count = 0;
        
        for (auto log : logs) {
            if (log.back() <= 'z' and log.back() >= 'a') {
                result.insert(result.begin(), log);
                count+=1;
            } else {
                result.push_back(log);
            }
        }
        
        sort(result.begin(), result.begin() + count, compare);
        return result;
    }
};
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

## Solution - Lambda Sorting (tricky)

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs.sort(key = lambda log: self.get_key(log))
        return logs
    
    def get_key(self, log):
        _id, rest = log.split(" ", maxsplit = 1)
        if rest[0].isalpha():
            # fisrt element = 0, means letter list will always comes first
            return (0, rest, _id)
        else:
            return (1, None)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**
