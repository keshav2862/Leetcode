class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        ans = [0]*n
        stack = []
        for i in range(n-1,-1,-1):
            h = heights[i]
            v = 0
            while stack and h>stack[-1]:
                stack.pop()
                v= v+1
            if stack:
                v=v+1
            ans[i] = v
            stack.append(h)
        return ans