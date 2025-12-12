class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        v = set()
        def dfs(r, c, k):
            if k == len(word):
                return True
            if not (0<=r<row) or not (0<=c<col) or (r,c) in v or board[r][c] != word[k]:
                return False
            v.add((r,c))
            a = dfs(r+1,c,k+1) or dfs(r-1, c, k+1) or dfs(r, c+1, k+1) or dfs(r, c-1, k+1)
            v.remove((r,c))
            return a
        # count = {}
        # for c in word:
        #     count[c] = 1 + count.get(c, 0)
        # if count[word[0]] > count[word[-1]]:
        #     word = word[::-1]
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0): return True        
        return False