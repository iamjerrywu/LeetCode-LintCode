# ArrayList 385 \(E\)

## Problem



Implement an ArrayListManager which can:

1. `create(n)`. Create an ArrayList of integers contains \[0, 1, 2, ... n-1\]
2. `clone(list)`. Clone a list. The cloned list should independent with the original list.
3. `get(list, index)`. Get the element on the _index_ position of the list.
4. `set(list, index, val)`. Change the value the element of _index_ position to given _val_.
5. `remove(list, index)`. Remove the element on the _index_ position.
6. `indexOf(list, val)`. Find the first index of element that equals to _val_ and return its index.

Please use the methods provided by _ArrayList_. See documents：[ArrayList Document](https://docs.oracle.com/javase/7/docs/api/java/util/ArrayList.html)Example

Input:

```text
create(5)
get([0,1,2,3,4], 0)
get([0,1,2,3,4], 1)
get([0,1,2,3,4], 4)
clone([0,1,2,3,4])
get([0,1,2,3,4], 2)
indexOf([0,1,2,3,4], 1)
indexOf([0,1,2,3,4], 10)
remove([0,1,2,3,4], 3)
get([0,1,2,4], 3)
set([0,1,2,4], 2, 3)
get([0,1,2,3,4], 2)
get([0,1,2,3,4], 3)
```

Output:

```text
[0,1,2,3,4]
0
1
4
[0,1,2,3,4]
2
1
-1
[0,1,2,4]
4
[0,1,3,4]
2
3
```

Explanation:

The code for java is like this:

```text
ArrayList<Integer> list = ArrayListManager.create(5);
list.get(0);  // should return 0
list.get(1);  // should return 1
list.get(4);  // should return 4

// clone_list should be [0,1,2,3,4]
ArrayList<Integer> clone_list = ArrayListManager.clone(list);

ArrayListManager.get(list, 2);  // should return 2
ArrayListManager.indexOf(list, 1); // should return 1
ArrayListManager.indexOf(list, 10); // should return -1
ArrayListManager.remove(list, 3); // list will become [0, 1, 2, 4]
ArrayListManager.get(list, 3); // as 3 has been removed, should return 4
ArrayListManager.set(list, 2, 3); // list will become [0, 1, 3, 4]

clone_list.get(2); // should return 2
clone_list.get(3); // should return 3
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

