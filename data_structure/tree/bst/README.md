# BST

## What's BST?

Definition:

* Left node is smaller than root node&#x20;
* RIght node is bigger/equal to root node
* Do in-order traversal, then it's an "**not descending" **order
* If a binary tree in-order traversal is not a "not descending" order, then it's definitely not a BST
* If a binary tree in-order traversal is a "not descending" order, then it might not be a BST
  * i.e.:    1      it's not a BST
  * &#x20;       /   \\
  * &#x20;      1    1
* For BST insertion worst case: (i.e: giving \[1,2,3,4,5], build up BST)
  * The time complexity is O(n^2)
    * Even BST height is logn, but that's in **balanced** condition

## BST CRUD

### Node Definition

{% tabs %}
{% tab title="Python" %}
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
```
{% endtab %}

{% tab title="Java" %}
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

### Retrieve

{% tabs %}
{% tab title="Python" %}
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

{% tab title="Java" %}
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

### Update

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

{% tab title="Java" %}
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

### Create

{% tabs %}
{% tab title="Python" %}
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

{% tab title="Java" %}
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

### Delete

{% tabs %}
{% tab title="Python" %}
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

{% tab title="Java" %}
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

### Create





## Red-Black Tree

A balanced BST

* O(logn) to do **CRUD**
* O(logn) to find max/min
* O(logn) to find the max that smaller than x / min that larger than x
* In Java 1.8 HashMap use both TreeMap/LinkedList to implement
  * If length > 8, than TreeMap is more effective than linked list
    * Since log8 < 8
