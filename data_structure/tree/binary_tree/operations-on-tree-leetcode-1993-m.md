# Operations on Tree \(LeetCode 1993\) \(M\)

## Problem

You are given a tree with `n` nodes numbered from `0` to `n - 1` in the form of a parent array `parent` where `parent[i]` is the parent of the `ith` node. The root of the tree is node `0`, so `parent[0] = -1` since it has no parent. You want to design a data structure that allows users to lock, unlock, and upgrade nodes in the tree.

The data structure should support the following functions:

* **Lock:** **Locks** the given node for the given user and prevents other users from locking the same node. You may only lock a node if the node is unlocked.
* **Unlock: Unlocks** the given node for the given user. You may only unlock a node if it is currently locked by the same user.
* **Upgrade: Locks** the given node for the given user and **unlocks** all of its descendants. You may only upgrade a node if **all** 3 conditions are true:
  * The node is unlocked,
  * It has at least one locked descendant \(by **any** user\), and
  * It does not have any locked ancestors.

Implement the `LockingTree` class:

* `LockingTree(int[] parent)` initializes the data structure with the parent array.
* `lock(int num, int user)` returns `true` if it is possible for the user with id `user` to lock the node `num`, or `false` otherwise. If it is possible, the node `num` will become **locked** by the user with id `user`.
* `unlock(int num, int user)` returns `true` if it is possible for the user with id `user` to unlock the node `num`, or `false` otherwise. If it is possible, the node `num` will become **unlocked**.
* `upgrade(int num, int user)` returns `true` if it is possible for the user with id `user` to upgrade the node `num`, or `false` otherwise. If it is possible, the node `num` will be **upgraded**.

**Example 1:**![](https://assets.leetcode.com/uploads/2021/07/29/untitled.png)

```text
Input
["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
[[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
Output
[null, true, false, true, true, true, false]

Explanation
LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]);
lockingTree.lock(2, 2);    // return true because node 2 is unlocked.
                           // Node 2 will now be locked by user 2.
lockingTree.unlock(2, 3);  // return false because user 3 cannot unlock a node locked by user 2.
lockingTree.unlock(2, 2);  // return true because node 2 was previously locked by user 2.
                           // Node 2 will now be unlocked.
lockingTree.lock(4, 5);    // return true because node 4 is unlocked.
                           // Node 4 will now be locked by user 5.
lockingTree.upgrade(0, 1); // return true because node 0 is unlocked and has at least one locked descendant (node 4).
                           // Node 0 will now be locked by user 1 and node 4 will now be unlocked.
lockingTree.lock(0, 1);    // return false because node 0 is already locked.
```

**Constraints:**

* `n == parent.length`
* `2 <= n <= 2000`
* `0 <= parent[i] <= n - 1` for `i != 0`
* `parent[0] == -1`
* `0 <= num <= n - 1`
* `1 <= user <= 104`
* `parent` represents a valid tree.
* At most `2000` calls **in total** will be made to `lock`, `unlock`, and `upgrade`.

## Solution - Brute Force Traversal

Build up the ancestor and descendant list of each node, then do the simulation according to the question

{% tabs %}
{% tab title="Python" %}
```python
import collections
class LockingTree:
 
    def __init__(self, parent: List[int]):
        n = len(parent)
        
        # build up ancestor tree
        self.ancestors = {}
        for i in range(len(parent)):
            ancestor_list = []
            node = i
            while parent[node] != -1:
                ancestor_list.append(parent[node])
                node = parent[node]
            
            self.ancestors[i] = sorted(list(ancestor_list))
        
        # build up descendant tree
        self.descendants = collections.defaultdict(list)
        for i in range(len(parent)):
            if parent[i] == -1:
                continue
            self.descendants[parent[i]].append(i)
        # print(self.descendants)    
        self.node_lock_state = {}
  
    def lock(self, num: int, user: int) -> bool:
        if num not in self.node_lock_state:
            self.node_lock_state[num] = user
            return True
        return False          

    def unlock(self, num: int, user: int) -> bool:
        if num in self.node_lock_state and self.node_lock_state[num] == user:
            self.node_lock_state.pop(num)
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if num not in self.node_lock_state:
            # check ancestors
            for ancestor in self.ancestors[num]:
                # since all ancestor should be unlock
                if ancestor in self.node_lock_state:
                    return False
            # check decedants
            cnt = 0
            queue = collections.deque()
            for decedant in self.descendants[num]:
                queue.append(decedant)
            while queue:
                node = queue.popleft()
                if node in self.descendants:
                    for decedant in self.descendants[node]:
                        queue.append(decedant)
                if node in self.node_lock_state:
                    cnt+=1
                    self.node_lock_state.pop(node) 
            # since at least one descendant should be lock
            if cnt == 0:
                return False
            self.node_lock_state[num] = user
            return True
        return False
            
            


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
```
{% endtab %}
{% endtabs %}

### Complexity Analysis

* **Time Complexity:** 
* **Space Complexity:** 

