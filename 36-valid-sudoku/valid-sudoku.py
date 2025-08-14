class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def valid_row(r):
            d1 = {}
            for el in r:
                if el in d1 and el != '.':
                    return False
                d1[el] = 1
            return True
        
        def valid_col(c, board):
            l1 = [board[i][c] for i in range(len(board))]
            d1 = {}
            for el in l1:
                if el in d1 and el != '.':
                    return False
                d1[el] = 1
            return True

        def valid_grid(row, col, board):
            d1 = {}
            for i in range(row, row +3):
                for j in range(col, col + 3):
                    if board[i][j] in d1 and board[i][j] != '.':
                        return False
                    d1[board[i][j]] = 1
            return True


        for row in board:
            bool1 = valid_row(row)
            if bool1 == False:
                return False
        
        for col in range(len(board[0])):
            bool2 = valid_col(col, board)
            if bool2 == False:
                return False

        for row in range(0, len(board), 3):
            for col in range(0, len(board[0]), 3):
                bool3 = valid_grid(row, col ,board)
                if bool3 == False:
                    return False
        return True        