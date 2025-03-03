class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.minHeap = []
        for num in nums:
            self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heapq.heapreplace(self.minHeap, val)
        return self.minHeap[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)