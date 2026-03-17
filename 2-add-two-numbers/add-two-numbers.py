# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2 or carry:
            val = carry
            if l1:
                val = val + l1.val
                l1 = l1.next
            if l2:
                val = val+l2.val
                l2 = l2.next
            carry,val = divmod(val,10)
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next