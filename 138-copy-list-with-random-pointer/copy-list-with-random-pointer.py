"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        node = head
        hmap = {}
        while node:
            hmap[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            if node.next:
                hmap[node].next = hmap[node.next]
            if node.random:
                hmap[node].random = hmap[node.random]
            node = node.next
        return hmap[head]

        