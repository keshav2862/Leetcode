# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        nh = dummy
        curr = head
        while curr:
            if curr.val<x:
                nh.next = ListNode(curr.val)
                nh = nh.next
            curr = curr.next
        node = head
        while node:
            if node.val==x or node.val>x:
                nh.next = ListNode(node.val)
                nh = nh.next
            node = node.next
        return dummy.next
