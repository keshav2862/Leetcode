
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        return heapq.nlargest(k, freq.keys(), key=lambda x: freq[x])