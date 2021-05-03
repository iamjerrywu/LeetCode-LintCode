# Attendance Judgment 1154 \(E\)

## Problem

Given A string representing a student's attendance, 'A' stands for attendance, 'D' for default, and 'L' for lateness. If the student is default for two and more times or he is late for three and more consecutive times, he should be punished. Please judge whether the student should be punished or not and return a Boolean type.

The string contains only 'A ',' D' and 'L' three types uppercase letters.  
The string length does not exceed 10000.Example

Input1: "AADALLLAD"  
Output1: true  
Explanation1: The student was default twice and was late three times in a row, so he should be punished.

Input2: "AADALLLA"  
Output2: true  
Explanation2: The student was only default once, but he was late three times in a row, so he should be punished.

Input3: "AADALLAAL"  
Output3: false  
Explanation3: The student was only default once and he was just late two times in a row at most, so he should not be punished.

## Solution 

### Code

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    """
    @param record: Attendance record.
    @return: If the student should be punished return true, else return false. 
    """
    def judge(self, record):
        # Write your code here.
        bad = {}
        for i in range(len(record)):
            if record[i] == 'D':
                bad['D'] = bad.get('D', 0) + 1
                if bad['D'] == 2:
                    return True
                bad['L'] = 0
            elif i > 0 and record[i - 1] == "L" and record[i] == "L":
                bad['L'] = bad.get('L', 0) + 1
                if bad['L'] == 2:
                    return True
            else:
                bad['L'] = 0
        return False
```
{% endtab %}

{% tab title="java" %}
```

```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

