class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        hashmap = defaultdict(int)
        for row in grid:
            rs = str(row)
            hashmap[rs] +=1
        c = 0
        for j in range(len(grid)):
            col = [grid[i][j] for i in range(len(grid))]
            cs = str(col)
            c = c + hashmap[cs]
        return c