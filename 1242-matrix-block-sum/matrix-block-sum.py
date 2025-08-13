class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        r = len(mat)
        c = len(mat[0])
        answers = [[-1 for i in range(c)] for j in range(r)]

        prefix = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(r):
            for j in range(c):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )
        for row in range(r):
            for col in range(c):
                row_left = row - k if k<=row else 0
                row_right = row + k if row + k < r else r - 1
                col_right = col + k if col + k < c else c - 1
                col_left = col - k if k<=col else 0
                answers[row][col] = (
                        prefix[row_right + 1][col_right + 1]
                        - prefix[row_left][col_right + 1]
                        - prefix[row_right + 1][col_left]
                        + prefix[row_left][col_left]
                    )
        return answers
