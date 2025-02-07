class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        s1 = set(nums1) - set(nums2)
        s2 = set(nums2) - set(nums1)
        n1 = [list(s1),list(s2)]
        return n1