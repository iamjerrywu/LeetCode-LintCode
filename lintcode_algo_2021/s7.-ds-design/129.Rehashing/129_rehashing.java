/**
 * Definition for ListNode
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param hashTable: A list of The first node of linked list
     * @return: A list of The first node of linked list which have twice size
     */    
    public ListNode[] rehashing(ListNode[] hashTable) {
        // write your code here
        int new_size = hashTable.length * 2;
        // System.out.println(new_size);
        ListNode[] res = new ListNode[new_size];
        
        for (int i = 0; i < hashTable.length; i++) {
            while (hashTable[i] != null) {
                int index = hashTable[i].val % new_size;
                // in Java: MOD act different in negative value
                // here in hash table, -7 should be in index:3 if hash table size = 5
                // but java -7 mod 5 = -3, therefore should add table size to let it = 3
                if (index < 0) {
                    index = index + new_size;
                }
                if (res[index] != null) {
                    handleCollision(hashTable[i], res, new_size);
                } else {
                    res[index] = new ListNode(hashTable[i].val);
                }
                hashTable[i] = hashTable[i].next;
            } 
        }
        return res;
    }

    private void handleCollision(ListNode node, ListNode[] res, int new_size) {
        int index = node.val % new_size;
        if (index < 0) {
            index = index + new_size;
        }
        ListNode cur = res[index];
        while (cur.next != null) {
            cur = cur.next;
        }
        cur.next = new ListNode(node.val);
    }
};