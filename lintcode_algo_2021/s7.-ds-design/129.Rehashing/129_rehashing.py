"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        new_size = len(hashTable) * 2
        res = [None] * new_size
        for item in hashTable:
            while item:
                if res[item.val%new_size]:
                    self.handle_collision(item, res, new_size)
                else:
                    res[item.val%new_size] = ListNode(item.val)
                item = item.next
        return res
    
    def handle_collision(self, item, res, new_size):
        cur = res[item.val%new_size]
        while cur.next:
            cur = cur.next
        cur.next = ListNode(item.val)