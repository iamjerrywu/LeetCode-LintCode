# BST

## What's BST?

Definition:

* Left node is smaller than root node 
* RIght node is bigger/equal to root node
* Do in-order traversal, then it's an "**not descending"** order
* If a binary tree in-order traversal is not a "not descending" order, then it's definitely not a BST
* If a binary tree in-order traversal is a "not descending" order, then it might not be a BST
  * i.e.:    1      it's not a BST
  *         /   \
  *        1    1
* For BST insertion worst case: \(i.e: giving \[1,2,3,4,5\], build up BST\)
  * The time complexity is O\(n^2\)
    * Even BST height is logn, but that's in **balanced** condition

## Red-Black Tree

A balanced BST

* O\(logn\) to do **CRUD**
* 
