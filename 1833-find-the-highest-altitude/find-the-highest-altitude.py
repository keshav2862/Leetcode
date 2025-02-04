class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        gl = list(gain)
        print(gl)
        ans=[0]*(len(gl)+1)
        i=0
        while i < len(gl):
            if i == 0:
                ans[i] = 0
                ans[i+1] = gl[i]
            else:
                ans[i+1] = ans[i] + gl[i]
            i=i+1
        return max(ans)