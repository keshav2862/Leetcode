from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)
        ans = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [key for key, val in ans[:k]]