class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        top = 0
        bot = l-1 
        while top < bot:
            for col in range(l):
                temp = matrix[top][col]
                matrix[top][col] = matrix[bot][col]
                matrix[bot][col] = temp
            top = top +1
            bot = bot -1
        for row in range(l):
            for col in range(row+1,l):
                temp = matrix[row][col]
                matrix[row][col]= matrix[col][row]
                matrix[col][row] = temp
        return matrix
        
                