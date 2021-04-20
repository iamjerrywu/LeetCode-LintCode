# BFS

## BFS

Application domain:

* Level traversal
  * Traverse over graph, tree, matrix
  * Shortest path
    * In graph every edge should be same length
* Connective components
  * Find all the connected vertices to one specific vertex 
  * Find all solution for one problem but not using recursion
* Tropological sorting 
  * Easier than BFS

![](../../.gitbook/assets/capture%20%283%29.png)

### Applicable Scenarios

#### Shortest Path:

* BFS

#### Longest Path:

* DP: if graph can be stratified \(path is directional and no loop\)
* DFS: If graph cannot be stratified

### Template

{% tabs %}
{% tab title="Python" %}
```python
# init
# put first node into queue (if multiple nodes, put them inside as well)
# first node distance as 0
# the distance record two things: 1: whether is visited / 2: the distance to that node
queue = collections.deque([node[)
distance ={node : 0}

# Keep visiting queue
while queue:
    node = queue.popleft()
    # extend the queue
    # pop out node's neighbors, then add them into queue and also update the distance
    for neighbor in node.get_neighbors():
        if neighbor in distance:
            continue
        distance[neighbor] = distance[node] + 1
        queue.append(neighbor)
```
{% endtab %}
{% endtabs %}

## Queue

Queue is a FIFO \(first in first out\) data structure, and widely used in BFS \(breadth-first-search\)

There are two ways to implement queue:

* **Array**: Better in randomly search for index \(since array is orderly stored in memory\)
* **LinkedList**: Better in insert/delete elements in queue

{% hint style="danger" %}
**Python:**  
Recommend to use `deque` instead of `Queue`, Since `Queue` implemented mutex \(lock\) for multi-threading

**Java:**  
Recommend to use `new ArrayDeque` , but not `new LinkedList`, Since LinkedList is slower
{% endhint %}

## Java Interface 

### Set

Set emphasizes on unique, like if trying to search any existed values, using set the best storage container

#### HashSet

* No repeated values
* Can have null value 
* Unordered
* Access faster O\(1\)

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

* No repeated values
* Can't not have null value 
* Ordered 
* Access slower O\(logn\)

{% code title="TreeSet" %}
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
{% endcode %}

### Map

Map is a type of fast key lookup data structure that offers flexible means of indexing into its individual elements. Key's non-repetitive. 

#### HashMap

* Key non-repetitive, value repetitive
* Key/value can be "null"
* unordered 

{% code title="HashMap" %}
```java
public class Solution {
    public static void main(String[] args){
        Map<String, String> map = new HashMap<>();
        for (int i = 5; i > 0; i --) {
            map.put(i + "", i + "");
        }
        map.put("1","1");//key non-repetitive
        map.put("11","1");//value repetitive
        map.put(null, null);//can be null
        for (Iterator i = map.keySet().iterator(); i.hasNext(); ) {
            String key = (String)i.next();
            String value = map.get(key);
            System.out.println("key = " + key + ", value = " + value);
        }
    }
}
//output
/*
key = 11, value = 1
key = null, value = null
key = 1, value = 1
key = 2, value = 2
key = 3, value = 3
key = 4, value = 4
key = 5, value = 5
*/
//unordered output
```
{% endcode %}

#### TreeMap

* Key non-repetitive, value repetitive
* Key/value cannot be "null"
* Ordered 

{% code title="TreeMap" %}
```java
public class Solution {
    public static void main(String[] args){
        Map<String, String> map = new TreeMap<>();
        for (int i = 5; i > 0; i --) {
            map.put(i + "", i + "");
        }
        map.put("1","1");//key non-repetitive
        map.put("11","1");//value repetitive
        //map.put(null, null);//null value
        for (Iterator i = map.keySet().iterator(); i.hasNext(); ) {
            String key = (String)i.next();
            String value = map.get(key);
            System.out.println("key = " + key + ", value = " + value);
        }
    }
}
//ouput
/*
key = 1, value = 1
key = 11, value = 1
key = 2, value = 2
key = 3, value = 3
key = 4, value = 4
key = 5, value = 5
*/
//ordered output
```
{% endcode %}

### List

List is ordered and repetition and null value allowed data structure. In Java there are **LinkedList** and **ArrayList**

#### LinkedList:

* Based on linked-list

**ArrayList:** 

* Based on dynamic arrays

**LinkedList vs ArrayList:**

* For randomly access like **get/set**, ArrayList O\(1\) better than LinkedList O\(n\)
* For new/delete like **add, remove**, if already know which index need to modify:
  * LinkedList O\(1\) better than ArrayList O\(n\), since ArrayList need moving elements

### Queue

Queue is a FIFO \(first in first out\) data structure, use enqueue to add value from tail, and remove from head 

#### PriorityQueue:

* Based on "Heap" 
* Non-FIFO

#### Queue:

* Based on Linked-List
* FIFO

## Graph

### Adjacent matrix

Following matrix means vertex 0 connect vertex 3, vertex 1 connect vertex 2. This data structure require O\(n^2\) space

\[ \[1,0,0,1\],   
  \[0,1,1,0\],   
  \[0,1,1,0\],   
  \[1,0,0,1\] \]  
\]

### Adjacent List

Following matrix means vertex 0 connect to vertex 1, vertex 1 connect to vertex 2, vertex 1 connect to vertex 3. The total edges amount = m, and space complexity is O\(m\). For worst case is O\(n^2\), however, that's rare case

\[  
 \[1\],  
 \[0,2,3\],  
 \[1\],  
 \[1\]  
\]

{% code title="In Java can use HashMap / HashSet to realize adjacent list" %}
```java
Map<T, Set> = new HashMap<Integer, HashSet>();
```
{% endcode %}

{% code title="Python can use dictionary comprehension" %}
```python
adjacency_list = {x:set() for x in nodes}
```
{% endcode %}

## Double Direction BFS

### Template 



![](../../.gitbook/assets/capture%20%284%29.png)



