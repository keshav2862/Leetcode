# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        ld = self.deepcheck(root.left)
        rd = self.deepcheck(root.right)
        
        if ld == rd:
            return (1 << ld) + self.countNodes(root.right)
        else:
            return (1 << rd) + self.countNodes(root.left)
    
    def deepcheck(self, node):
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth        