# Employee Importance \(LeetCode 690\) \(M\)

## Problem

You have a data structure of employee information, which includes the employee's unique id, their importance value, and their direct subordinates' id.

You are given an array of employees `employees` where:

* `employees[i].id` is the ID of the `ith` employee.
* `employees[i].importance` is the importance value of the `ith` employee.
* `employees[i].subordinates` is a list of the IDs of the subordinates of the `ith` employee.

Given an integer `id` that represents the ID of an employee, return _the total importance value of this employee and all their subordinates_.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/05/31/emp1-tree.jpg)

```text
Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11
Explanation: Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3.
They both have importance value 3.
So the total importance value of employee 1 is 5 + 3 + 3 = 11.
```

**Example 2:**![](https://assets.leetcode.com/uploads/2021/05/31/emp2-tree.jpg)

```text
Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
Output: -3
```

**Constraints:**

* `1 <= employees.length <= 2000`
* `1 <= employees[i].id <= 2000`
* All `employees[i].id` are **unique**.
* `-100 <= employees[i].importance <= 100`
* One employee has at most one direct leader and may have several subordinates.
* `id` is guaranteed to be a valid employee id.

## Solution 

{% tabs %}
{% tab title="Python" %}
```python
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

import collections
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees_record = {}
        for employee in employees:
            employees_record[employee.id] = [employee.importance, employee.subordinates]
        
        
        queue = collections.deque()
        ans = 0
        queue.append(id)
    
        while queue:
            person = queue.popleft()
            ans+=employees_record[person][0]
            for subordinate in employees_record[person][1]:
                queue.append(subordinate)
        
        return ans
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:** 
* **Space Complexity:** 

