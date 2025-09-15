# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.postroot = len(postorder)-1
        hmap = {val: x for x,val in enumerate(inorder)}
        def finder(left,right):
            if left>right:
                return None
            k = postorder[self.postroot]
            self.postroot -= 1
            root = TreeNode(k)
            idx = hmap[k]
            root.right = finder(idx+1,right)
            root.left = finder(left,idx -1)
            return root
        return finder(0, len(inorder)-1)
