# W5. Traverse/D&C/DFS

## Recursion vs DFS vs Back Tracking

### Recursion

* **Recursion Function**
  * Kind of programming that function call itself
* **Recursion algorithm**
  * Big problems rely on small problem's result, and use recursion function to solve small problem

### Depth First Search \(DFS\)

* Can implement using recursion 
* Can also use stack to implement without using recursion 
* DFS means when searching first search the deeper nodes but not the same layer nodes
  * Take BST, pre-order traverse is DFS

### Back Tracking

* Back tracking is DFS 
* Recursion function's value need to roll back to previous recursion function's version

  * For example, when traversing BST recording path
    * After adding node 3 and return back to node 1, should pop node 3 and add node 4
      * If not popping node 3, then path would be \[1, 3, 4\], which  

                               1  
                             /   \  
                           3      4

## BST Traversal vs Divide Conquer

Both of them can use DFS to implement, but there are some difference

* Traversal: 
  * Have to traverse all the nodes itself, and record the values \(require heap memory usage\)
* Divide and Conquer:
  * Traverse from left/right tree, then eventually merge the left/right tree's results
  * It's **Post-Traversal** \(left child -&gt; right child -&gt; parent\)

## BST Divide and Conquer Template

{% tabs %}
{% tab title="python" %}
```java
public returntype divideConquer(TreeNode root) {
    if (root == null) {
        process if empty tree
    }
    
    // if (root.left == null && root.right == null) {
    // process when encounter leaf
    // }
    
    left tree return result = divideConquer(root.left)
    right tree return result = divideConquer(root.right)
    whole tree return result = merge two tree result 
    
    return whole tree result
}
```
{% endtab %}
{% endtabs %}



