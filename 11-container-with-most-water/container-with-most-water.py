class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        start = 0
        end = n-1
        i = 0
        area = []
        while i < n:
            h = min(height[start],height[end])
            l = end - start
            area.append(l*h)
            if height[start] > height[end]:
                end = end -1
            else:
                start = start + 1
            i = i+1
        return max(area)