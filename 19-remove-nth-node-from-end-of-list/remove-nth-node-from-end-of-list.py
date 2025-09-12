# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        l = 0
        current = head
        while current:
            l = l+1
            current = current.next
        current = dummy 
        for i in range(l-n):
            current = current.next
        current.next = current.next.next
        return dummy.next
        