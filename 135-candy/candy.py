class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = [1] * len(ratings)
        sum =0
        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                res[i+1] = res[i]+1
        for j in range(len(ratings)-1,0,-1):
            if ratings[j-1] > ratings[j] and res[j-1] <= res[j]:
                res[j-1] = res[j]+1
        for k in range(len(res)):
            sum = sum + res[k]
        return sum