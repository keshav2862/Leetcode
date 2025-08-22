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
        root = n = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry = carry + l1.val
                l1 = l1.next
            if l2:
                carry = carry + l2.val
                l2 = l2.next
            carry, val = divmod(carry,10)
            n.next = ListNode(val)
            n = n.next
        return root.next