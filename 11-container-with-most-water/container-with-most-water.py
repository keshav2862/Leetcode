class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        s= 0
        e = n-1
        i = 0
        area = 0
        while s < e:
            h = min(height[s],height[e])
            l = e - s
            area = max(area,l*h)
            if height[s] < height[e]:
                s = s+1
            else:
                e = e-1
        return area
                
