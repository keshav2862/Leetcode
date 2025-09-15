# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.preroot = 0
        hmap = {val: x for x,val in enumerate(inorder)}
        def finder(left,right):
            if left>right:
                return None
            k = preorder[self.preroot]
            self.preroot += 1
            root = TreeNode(k)
            idx = hmap[k]
            root.left = finder(left,idx -1)
            root.right = finder(idx+1,right)
            return root
        return finder(0, len(inorder)-1)

        