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
     * @param root: The root of binary tree.
     * @return: True if this Binary tree is Balanced, or false.
     */
    class Res {
    public boolean isBalanced;
    public int height;
    public Res(boolean isBalanced, int height) {
        this.isBalanced = isBalanced;
        this.height = height;
    }
}
    
    public boolean isBalanced(TreeNode root) {
        // write your code here
        Res result= validate(root);
        return result.isBalanced;
    }

    private Res validate(TreeNode root) {
        if (root == null) {
            return new Res(true, 0);
        }

        Res leftRes = validate(root.left);
        Res rightRes = validate(root.right);
        int rootHeight = Math.max(leftRes.height, rightRes.height) + 1;

        if (!leftRes.isBalanced || !rightRes.isBalanced) {
            return new Res(false, rootHeight);
        }
        if (Math.abs(leftRes.height - rightRes.height) > 1) {
            return new Res(false, rootHeight);
        }
        return new Res(true, rootHeight);
        
    }
}