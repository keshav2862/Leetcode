# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head
        node = head
        l = 0
        while node:
            l = l+1
            tail = node
            node = node.next
        k = k % l
        if k == 0:
            return head
        tail.next = head
        nt = head
        for i in range(l-k-1):
            nt = nt.next
        nh = nt.next
        nt.next = None
        return nh
        
