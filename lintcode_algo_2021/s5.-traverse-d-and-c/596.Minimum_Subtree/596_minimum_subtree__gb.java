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
 */

public class Solution {
    /**
     * @param root: the root of binary tree
     * @return: the root of the minimum subtree
     */
    private int minSum;
    private TreeNode minRoot;
    public Solution() {
       minSum = Integer.MAX_VALUE;
       minRoot = null; 
    }
    public TreeNode findSubtree(TreeNode root) {
        // write your code here
        getSum(root);
        
        return minRoot;
    }

    private int getSum(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int leftWeight = getSum(root.left);
        int rightWeight = getSum(root.right);
        int rootWeight = leftWeight + rightWeight + root.val;

        if (rootWeight < minSum) {
            minSum = rootWeight;
            minRoot = root;
        }
        return rootWeight;
    }
}