class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n =len(heights)
        stack = []
        ans = 0
        for i in range(n):
            val = heights[i]
            while stack and heights[stack[-1]] > val:
                idx = stack.pop()
                width = (i-stack[-1]-1) if stack else i
                ans = max(ans,(heights[idx]*width))
            stack.append(i)
        while stack:
            idx = stack.pop()
            width = (n - stack[-1] - 1) if stack else n
            ans = max(ans,(heights[idx]*width))
            
        return ans