# Technics

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





