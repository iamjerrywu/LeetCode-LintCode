# Technics

## Queue

Queue is a FIFO \(first in first out\) data structure, and widely used in BFS \(breadth-first-search\)

There are two ways to implement queue:

* **Array**: Better in randomly search for index \(since array is orderly stored in memory\)
* **LinkedList**: Better in insert/delete elements in queue

## Java Interface 

### Set

#### HashSet

No repeated values / **Can have null value / unordered**

{% code title="HashSet" %}
```java
Set<String> set = new HashSet<>();
for (int i = 1; i < 6; i ++) {
	set.add(i + "");
}
set.add("1"); //no effect since repeated value
set.add(null);//write "null"
Iterator<String> iter = set.iterator();
while (iter.hasNext()) {
	system.out.print(iter.next() + " ");//unordered 
}// output unordered as: 3 4 1 5 null 2
```
{% endcode %}

#### TreeSet

No repeated values / **Can't not have null value / ordered**

```java
Set<String> set = new TreeSet<>();
for (int i = 1; i < 6; i ++) {
	set.add(i + "");
}
set.add("1"); //no effect since repeated value
//set.add(null);//not allowed "null" value
Iterator<String> iter = set.iterator();
while (iter.hasNext()) {
	system.out.print(iter.next() + " ");//ordered
}// output ordered as: 1 2 3 4 5
```



