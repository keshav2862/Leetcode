class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        i = 0
        j = 0
        il = 0
        left = 0
        top = 0
        ans = []
        bottom = len(matrix) - 1
        for x in matrix:
            il = il + len(x)
        right = (il/(bottom+1)) - 1 
        print(left,right,bottom,top)
        while top <= bottom and left <=right:
            while j <= right:
                ans.append(matrix[top][j])
                j = j+1
            top = top + 1
            j = right
            i = i+1
            while i <= bottom:
                ans.append(matrix[i][right])
                i = i+1
            right = right - 1
            i = bottom
            j = j -1
            if top <= bottom:
                while j >= left:
                    ans.append(matrix[bottom][j])
                    j = j-1
                bottom = bottom -1
                j = left
                i = i-1
            if left <= right:
                while i >= top:
                    ans.append(matrix[i][left])
                    i = i-1
                left = left + 1
                j = j+1
                i = top
        return ans