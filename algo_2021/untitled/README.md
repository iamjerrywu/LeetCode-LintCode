# S7. Hash/Heap

## Hash \(Java\)

### HashMap vs HashSet

#### Background

Array is fast for accessing value \(via for loop\), but slow for storing \(with limited length\); linkedlist easy for storing but slow for accessing value. Hash table comes  to solve this disadvantage.

HashSet is implemented vai HashMap. HashMap has imput parameters as `Key`, `Value`. HashSet keep `Value` as constant, only manipulate `key`.

HashMap is build up by array which each value in array is tailed by a linkedlist. This is so called `Hash Table: Chaining`. 

### HashMap Principle

1. Input HashMap's `Key` to HashCode\(\), and return the hashCode \(int\)
2. Use this hashCode as index, to find it's mapping value in hash table. If that mapped value is Null, then import the HashMap's `Key`, `Value` as entry tuple, putting them in that index's location
3. It that mapped value is not Null, then search for the linkedlist tailing that index's location. Once find the same key as the one in entry tuple, then update the value.
4. If not finding the same key in the linkedlist, then shift the existed linkedlist backward, and make the new entry tuple as the head of that linkedlist

### HashSet Principle

1. When importing element into HashSet, HasSet would obtain hash value by importing element into HashCode\(\). Then based on that hash value, can calculate the location of that element. 
   1. First if that location have no element, then store that element to that location
   2. If that location is already occupied, then compare entry element with that one \(using `equals()`\)
      1. If return `true`, then they are the same, entry element is repeated one, cannot be added 
      2. If return `false`, then can add entry element inside

### Conclusion

| HashMap | HashSet |
| :--- | :--- |
| `Map` interface | `Set`interface |
| Store tuple | Store object |
| `put()`to add into map | `add()`to add into set |
| HashMap using Key to calculate HashCode | HashSet using object to calculate Hashcode. For two object their hashcode can be the same, use `equals()` to differentiate  \(return true if same/false if not\) |

## Heap

A Heap is a special Tree-based data structure in which the tree is a complete binary tree. Generally, Heaps can be of two types:

1. **Max-Heap \(Max Priority Queue\)**: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
2. **Min-Heap \(Min Priority Queue\)**: In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree

### Heap vs Priority Queue

Priority Queue is an abstract data structure, close to heap data structure. In Java, python there is already Priority Queue \(Heaps\). It support **Insert** and **DeleteMin** to operations. Mapping to heaps they are like **Enqueue**, **Dequeue**. 





