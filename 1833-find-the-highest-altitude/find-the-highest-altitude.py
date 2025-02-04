class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        gl = gain
        ans=[0]
        i=0
        while i < len(gl):
            ans.append(ans[i]+gl[i])
            i=i+1
        return max(ans)