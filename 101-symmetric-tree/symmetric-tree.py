# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def mirror(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and mirror(left.left,right.right) and mirror(left.right,right.left)
        return mirror(root.left,root.right)