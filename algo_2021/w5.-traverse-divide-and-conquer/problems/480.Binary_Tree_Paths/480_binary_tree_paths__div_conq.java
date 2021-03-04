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
     * @param root: the root of the binary tree
     * @return: all root-to-leaf paths
     */
    public List<String> binaryTreePaths(TreeNode root) {
        // write your code here
        List<String> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        if (root.left == null && root.right == null) {
            res.add("" + root.val);
            return res;
        }

        for (String leftPath : binaryTreePaths(root.left)) {
            res.add(root.val + "->" + leftPath);
        }
        for (String rightPath : binaryTreePaths(root.right)) {
            res.add(root.val + "->" + rightPath);
        }
        
        return res;
    }
}