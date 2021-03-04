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
        List<String> res = new ArrayList<String>();
        
        if (root == null) {
            return res;
        }
        String path = String.valueOf(root.val);
        return findPath(root, path, res);
    }
    
    private List<String> findPath(TreeNode node, String path, List<String> res) {
        if (node == null) {
            return res;
        }
        if(node.left == null && node.right == null) {
            res.add(path);
            return res;
        }

        if (node.left != null) {
            // this way that every time called function would create new apth string
            // total times would be: 1 + 2 + ...+ n -> space complexity: O(n^2) 
            findPath(node.left, path + "->" + node.left.val, res);
        }
        if (node.right != null) {
            findPath(node.right, path + "->" + node.right.val, res);
        }
        return res;
    }
}