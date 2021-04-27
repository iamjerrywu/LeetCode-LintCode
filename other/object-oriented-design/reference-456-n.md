# Reference 456 \(N\)

## Problem

Implement the class ReferenceManager. Include the following two methods:

1. `copyValue(Node obj)`. This would just copy the value from parameter _obj_ to the public attribute _node_. But _obj_ and _node_ are still two difference instances / objects.
2. `copyReference(Node obj)`. This would copy the reference from _obj_ to _node_. So that both _node_ and _obj_ are point to the same object.

Example

ReferenceManager ref = ReferenceManager\(\);  
Node obj = new Node\(0\);  
ref.copyValue\(obj\);  
ref.node.val; // will be 0  
ref.node; // will be different with obj.

```text
Node obj2 = new Node(1);
ref.copyReference(obj2);
ref.node.val; // will be 1
ref.node; // will be the same with obj2
```

## Solution

### Code

{% tabs %}
{% tab title="python" %}
```python

```
{% endtab %}

{% tab title="java" %}
```java
/**
 * Definition of Node:
 * class Node {
 *     public int val;
 *     public Node(int val) {
 *         this.val = val;
 *     }
 * }
 */
public class ReferenceManager {
    public Node node;

    public void copyValue(Node obj) {
        // copy value from obj to node
        if (obj == null) return;
        if (node == null) node = new Node(obj.val);
        // obj.val = node.val;
        
    }

    public void copyReference(Node obj) {
        // copy reference from obj to node
        node = obj;
    }
}
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:**
* **Space Complexity:**

