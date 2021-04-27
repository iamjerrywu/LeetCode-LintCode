# Student ID 455 \(E\)

## Problem



Description

Implement a class `Class` with the following attributes and methods:

1. A public attribute `students` which is a array of `Student` instances.
2. A constructor with a parameter n, which is the total number of students in this _class_. The constructor should create n Student instances and initialized with student id from _0_ ~ _n-1_

Example

**Example 1:**

```text
Input: 3
Output: [0, 1, 2]
Explanation: For 3 students, your cls.students[0] should equal to 0, cls.students[1] should equal to 1 and the cls.students[2] should equal to 2.
```

**Example 2:**

```text
Input: 5
Output: [0, 1, 2, 3, 4]
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python
class Student:
    def __init__(self, id):
        self.id = id;

class Class:

    '''
     * Declare a constructor with a parameter n which is the total number of
     * students in the *class*. The constructor should create n Student
     * instances and initialized with student id from 0 ~ n-1
    '''
    # write your code here
    def __init__(self,n):
        self.students = []
        for i in range(n):
            self.students.append(Student(i))
```
{% endtab %}

{% tab title="java" %}
```java
class Student {
    public int id;
    
    public Student(int id) {
        this.id = id;
    }
}

public class Class {
    /**
     * Declare a public attribute `students` which is an array of `Student`
     * instances
     */
    // write your code here.
    Student[] students;
     
    /**
     * Declare a constructor with a parameter n which is the total number of
     * students in the *class*. The constructor should create n Student
     * instances and initialized with student id from 0 ~ n-1
     */
    // write your code here
    public Class(int n) {
        students = new Student[n];
        for (int i = 0 ; i < n ; i ++ ) {
            students[i] = new Student(i);
        }
    }
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

