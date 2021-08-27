# Minimum Time Difference 1184 \(M\)

## Problem

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum **minutes** difference between any two time points in the list.

1.The number of time points in the given list is at least 2 and won't exceed 20000.  
2.The input time is legal and ranges from 00:00 to 23:59.Example

Example 1:

```text
Input:["23:59","00:00"]Output:1
```

Example 2:

```text
Input:["01:01","02:01"]Output:60
```

## Solution - Brute Force Enumeration

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ans = float('inf')
        for i in range(len(timePoints) - 1):
            for j in range(i + 1, len(timePoints)):
                ans = min(ans, self.cal_diff(timePoints[i], timePoints[j]))
        return ans
    
    def cal_diff(self, time1, time2):
        day_min = 24 * 60
        time_list = time1.split(":")
        time1_min = int(time_list[0]) * 60 + int(time_list[1])
        time_list = time2.split(":")
        time2_min = int(time_list[0]) * 60 + int(time_list[1])
        if time1_min > time2_min:
            time1_min, time2_min = time2_min, time1_min
        diff = min(abs(0 - time1_min) + abs(day_min - time2_min), abs(time1_min - time2_min))
        return diff
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(n^2\)**
* **Space Complexity: O\(1\)**

## Solution - Sorting

First transfer all the time into sec format, then sort the list. Afterwards, pick every two time to compare with each other, then finally compare the first and the last one

{% tabs %}
{% tab title="Python" %}
```python
class Solution:
    """
    @param timePoints: a list of 24-hour clock time points
    @return: the minimum minutes difference between any two time points in the list
    """
    def findMinDifference(self, timePoints):
        # Write your code here
        time_sec = []
        for time in timePoints:
            time_list = time.split(':')
            time_sec.append(int(time_list[0]) * 60 + int(time_list[1]))
        
        time_sec.sort()
        
        ans = float('inf')
        for i in range(len(time_sec) - 1):
            ans = min(ans, self.cal_diff(time_sec[i], time_sec[i + 1]))
        # need to compare the fisrt one with the last one
        ans = min(ans, self.cal_diff(time_sec[0], time_sec[-1]))

        return ans
    
    def cal_diff(self, time1, time2):
        day_sec = 24 * 60
        return min((time1 - 0) + (day_sec - time2), time2 - time1)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity: O\(nlogn\)**
* **Space Complexity: O\(n\)**

{% hint style="danger" %}
 LTE!
{% endhint %}

