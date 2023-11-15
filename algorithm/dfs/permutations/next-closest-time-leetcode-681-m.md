# Next Closest Time (LeetCode 681) (M)

## Problem

Given a `time` represented in the format `"HH:MM"`, form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, `"01:34"`, `"12:09"` are all valid. `"1:34"`, `"12:9"` are all invalid.

&#x20;

**Example 1:**

```
Input: time = "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.
```

**Example 2:**

```
Input: time = "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
```

&#x20;

**Constraints:**

* `time.length == 5`
* `time` is a valid time in the form `"HH:MM"`.
* `0 <= HH < 24`
* `0 <= MM < 60`

## Solution - Brute Force and Check

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        time_id = 0
        time_str = ""
        prev = time[0]
        same = True
        for i, c in enumerate(time):
            if c.isdigit():
                time_str+=c
                if c != prev:
                    same = False
            else:
                time_id = i
        if same:
            return time
        
        min_comb = ["", float('inf')]        
        self.dfs(time_str, time, "", time_id, min_comb)
        return min_comb[0]
    
    def dfs(self, time_str, time, new_time, time_id, min_comb):
        if len(new_time) == len(time):
            self.update(time, new_time, min_comb)
            return 
        
        for i in range(len(time_str)):
            if len(new_time) == time_id:
                self.dfs(time_str, time, new_time + ":", time_id, min_comb)
                return 
            self.dfs(time_str, time, new_time + time_str[i], time_id, min_comb)
           
    def update(self, time, new_time, min_comb):
        if time == new_time:
            return 
        # hrs
        time_hr = int(time.split(":")[0])
        new_time_hr = int(new_time.split(":")[0])
        if new_time_hr >= 24:
            return
        
        # mins
        time_min = int(time.split(":")[1])
        new_time_min = int(new_time.split(":")[1])
        if new_time_min >= 60:
            return
        
        new_time_int = 60 * new_time_hr + new_time_min
        time_int = 60 * time_hr + time_min
        
        if new_time_int < time_int:
            new_time_int+=60 * 24
        
        if abs(new_time_int - time_int) < min_comb[1]:
            min_comb[1] = abs(new_time_int - time_int)
            min_comb[0] = new_time
```
{% endtab %}

{% tab title="Java" %}
```java
```
{% endtab %}

{% tab title="C++" %}
```cpp
```
{% endtab %}
{% endtabs %}

* **Time Complexity:**
* **Space Complexity:**

