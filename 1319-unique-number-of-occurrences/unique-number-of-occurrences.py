class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}
        for x in arr:
            freq[x] = freq.get(x,0) + 1
        print(len(freq))
        return len(freq) == len(set(freq.values()))