class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        area = 0
        l = 0
        r = n-1
        lh = height[0]
        rh = height[n-1]
        while l<r:
            if lh<rh:
                l = l+1
                lh = max(lh,height[l])
                area += lh-height[l]
            else:
                r = r-1
                rh = max(rh,height[r])
                area += rh - height[r]
        return area
            



