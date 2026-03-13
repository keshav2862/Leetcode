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
        curr = head
        while curr:
            l = l+1
            curr = curr.next
        curr = dummy
        for i in range(l-n):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next