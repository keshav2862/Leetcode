class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        lr = len(matrix)
        lc = len(matrix[0])
        
        frowcheck = False
        fcolcheck = False

        for c in range(lc):
            if matrix[0][c] == 0:
                frowcheck = True
                break
        for r in range(lr):
            if matrix[r][0] == 0:
                fcolcheck = True
                break
        for r in range(1, lr):
            for c in range(1,lc):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1,lr):
            if matrix[r][0] == 0:
                for c in range(1,lc):
                    matrix[r][c]= 0
        for c in range(1,lc):
            if matrix[0][c] == 0:
                for r in range(1,lr):
                    matrix[r][c]= 0
        if frowcheck:
            for c in range(lc):
                matrix[0][c] = 0
        if fcolcheck:
            for r in range(lr):
                matrix[r][0] = 0
