# Alert Using Same Key-Card Three or More TIme in a One Hour Period \(LeetCode 1604\) \(M\)

## Problem

LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an **alert** if any worker uses the key-card **three or more times** in a one-hour period.

You are given a list of strings `keyName` and `keyTime` where `[keyName[i], keyTime[i]]` corresponds to a person's name and the time when their key-card was used **in a** **single day**.

Access times are given in the **24-hour time format "HH:MM"**, such as `"23:51"` and `"09:49"`.

Return a _list of unique worker names who received an alert for frequent keycard use_. Sort the names in **ascending order alphabetically**.

Notice that `"10:00"` - `"11:00"` is considered to be within a one-hour period, while `"22:51"` - `"23:52"` is not considered to be within a one-hour period.

**Example 1:**

```text
Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
Output: ["daniel"]
Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").
```

**Example 2:**

```text
Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
Output: ["bob"]
Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").
```

**Example 3:**

```text
Input: keyName = ["john","john","john"], keyTime = ["23:58","23:59","00:01"]
Output: []
```

**Example 4:**

```text
Input: keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"], keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
Output: ["clare","leslie"]
```

**Constraints:**

* `1 <= keyName.length, keyTime.length <= 105`
* `keyName.length == keyTime.length`
* `keyTime[i]` is in the format **"HH:MM"**.
* `[keyName[i], keyTime[i]]` is **unique**.
* `1 <= keyName[i].length <= 10`
* `keyName[i] contains only lowercase English letters.`

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        time_record = collections.defaultdict(list)
        prev_time_sec = 0
        for i in range(len(keyName)):
            # get time
            time_list = keyTime[i].split(':')
            time_sec = int(time_list[0]) * 60 + int(time_list[1])
            time_record[keyName[i]].append(time_sec)
            
        ans = []
        for key, time_list in time_record.items():
            # if shorter than 3, no way can alert happen
            if len(time_list) < 3:
                continue
            # since the list may not sorted
            time_list.sort()
            # compare every three between max and min
            for i in range(len(time_list) - 2):
                if time_list[i + 2] - time_list[i] <= 60:
                    ans.append(key)
                    break
        ans.sort()
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:  O\(nlogn\)**
  * n: length of either keyName/keyTime
* **Space Complexity:  O\(n\)**

