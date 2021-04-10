# S5. Traverse/D&C

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

## BST DFS

### BST Traversal vs Divide Conquer

Both of them can use DFS to implement, but there are some difference

* Traversal: 
  * Have to traverse all the nodes itself, and record the values \(require heap memory usage\)
* Divide and Conquer:
  * Traverse from left/right tree, then eventually merge the left/right tree's results
  * It's **Post-Traversal** \(left child -&gt; right child -&gt; parent\)

### BST Divide and Conquer Template

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

## BST  CRUD

### Tree Node Definition 

{% tabs %}
{% tab title="python" %}
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
```
{% endtab %}

{% tab title="java" %}
```java
class TreeNode{
	int val;
	TreeNode left;
	TreeNode right;
	pubic TreeNode(int val) {
		this.val = val;
		this.left = this.right = null;
	}
}
```
{% endtab %}
{% endtabs %}

### Node Retrieve

{% tabs %}
{% tab title="python" %}
```python
def searchBST(root, val):
    if not root:
        return None # 未找到值为val的节点
    if val < root.val:
        return searchBST(root.left, val) # val小于根节点值，在左子树中查找哦
    elif val > root.val:
        return searchBST(root.right, val) # val大于根节点值，在右子树中查找
    else:
        return root
```
{% endtab %}

{% tab title="java" %}
```java
public TreeNode searchBST(TreeNode root, int val) {
	if (root == null) {
		return null;
	}// 未找到值为val的节点
	if (val < root.val) {
		return searchBST(root.left, val);//val小于根节点值，在左子树中查找
	} else if (val > root.val) {
		return searchBST(root.right, val);//val大于根节点值，在右子树中查找
	} else {
		return root;//找到了
	}
}
```
{% endtab %}
{% endtabs %}

### Node Update

{% tabs %}
{% tab title="Python" %}
```python
def updateBSTBST(root, target, val):
    if not root:
        return  # 未找到target节点
    if target < root.val:
        updateBST(root.left, target, val) # target小于根节点值，在左子树中查找哦
    elif target > root.val:
        updateBST(root.right, target, val) # target大于根节点值，在右子树中查找
    else:  # 找到了
        root.val = val
```
{% endtab %}

{% tab title="java" %}
```java
public void updateBST(TreeNode root, int target, int val) {
	if (root == null) {
		return;
	}// 未找到target节点
	if (target < root.val) {
		updateBST(root.left, target, val);//target小于根节点值，在左子树中查找
	} else if (target > root.val) {
		updateBST(root.right, target, val);//target大于根节点值，在右子树中查找
	} else { //找到了
		root.val = val;
	}
}
```
{% endtab %}
{% endtabs %}

### Node Create

{% tabs %}
{% tab title="python" %}
```python
def insertNode(root, node):
    if not root:
        return node
    if root.val > node.val:
        root.left = insertNode(root.left, node)
    else:
        root.right = insertNode(root.right, node)
    return root
```
{% endtab %}

{% tab title="java" %}
```java
public TreeNode insertNode(TreeNode root, TreeNode node) {
    if (root == null) {
        return node;
    }
    if (root.val > node.val) {
        root.left = insertNode(root.left, node);
    } else {
        root.right = insertNode(root.right, node);
    }
    return root;
}
```
{% endtab %}
{% endtabs %}

### Node Delete

{% tabs %}
{% tab title="python" %}
```python
def removeNode(root, value):
    dummy = TreeNode(0)
    dummy.left = root
    parent = findNode(dummy, root, value)
    node = None
    if parent.left and parent.left.val == value:
        node = parent.left
    elif parent.right and parent.right.val == value:
        node = parent.right
    else:
        return dummy.left
    deleteNode(parent, node)
    return dummy.left

def findNode(parent, node, value):
    if not node:
        return parent
    if node.val == value:
        return parent
    if value < node.val:
        return findNode(node,node.left, value)
    else:
        return findNode(node, node.right, value)

def deleteNode(parent, node):
    if not node.right:
        if parent.left == node:
            parent.left = node.left
        else:
            parent.right = node.left
    else:
        temp = node.right
        father = node
        while temp.left:
            father = temp
            temp = temp.left
        if father.left == temp:
            father.left = temp.right
        else:
            father.right = temp.right
        if parent.left == node:
            parent.left = temp
        else:
            parent.right = temp
        temp.left = node.left
        temp.right = node.right
```
{% endtab %}

{% tab title="java" %}
```java
public TreeNode removeNode(TreeNode root, int value) {
    TreeNode dummy = new TreeNode(0);
    dummy.left = root;
    TreeNode parent = findNode(dummy, root, value);
    TreeNode node;
    if (parent.left != null && parent.left.val == value) {
        node = parent.left;
    } else if (parent.right != null && parent.right.val == value) {
        node = parent.right;
    } else {
        return dummy.left;
    }
    deleteNode(parent, node);
    return dummy.left;
}

private TreeNode findNode(TreeNode parent, TreeNode node, int value) {
    if (node == null) {
        return parent;
    }
    if (node.val == value) {
        return parent;
    }
    if (value < node.val) {
        return findNode(node, node.left, value);
    } else {
        return findNode(node, node.right, value);
    }
}

private void deleteNode(TreeNode parent, TreeNode node) {
    if (node.right == null) {
        if (parent.left == node) {
            parent.left = node.left;
        } else {
            parent.right = node.left;
        }
    } else {
        TreeNode temp = node.right;
        TreeNode father = node;
        while (temp.left != null) {
            father = temp;
            temp = temp.left;
        }
        if (father.left == temp) {
            father.left = temp.right;
        } else {
            father.right = temp.right;
        }
        if (parent.left == node) {
            parent.left = temp;
        } else {
            parent.right = temp;
        }
        temp.left = node.left;
        temp.right = node.right;
    }
}
```
{% endtab %}
{% endtabs %}

