/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 * Example of iterate a tree:
 * BSTIterator iterator = new BSTIterator(root);
 * while (iterator.hasNext()) {
 *    TreeNode node = iterator.next();
 *    do something for node
 * } 
 */


public class BSTIterator {
    /**
    * @param root: The root of binary tree.
    */
    private Stack<TreeNode> stack = new Stack<>();
    public BSTIterator(TreeNode root) {
        // do intialization if necessary
        while (root != null) {
            stack.push(root);
            root = root.left;
        }
    }

    /**
     * @return: True if there has next node, or false
     */
    public boolean hasNext() {
        // write your code here
        return !stack.isEmpty();
    }

    /**
     * @return: return next node
     */
    public TreeNode next() {
        // write your code here
        TreeNode cur = stack.peek();
        TreeNode node = cur;

        if (node.right == null) {
            node = stack.pop();
            while(!stack.isEmpty() && stack.peek().right == node) {
                node = stack.pop();
            }
        } else {
            node = node.right;
            while(node != null) {
                stack.push(node);
                node = node.left;
            }
        }
        return cur;
    }
}