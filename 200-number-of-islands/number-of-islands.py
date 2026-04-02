class Solution:
    def dfs(self, i,j,m,n,grid):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!='1':
                return
            grid[i][j] = 'visited'
            self.dfs(i-1,j,m,n,grid)
            self.dfs(i,j-1,m,n,grid)
            self.dfs(i+1,j,m,n,grid)
            self.dfs(i,j+1,m,n,grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(i,j,m,n,grid)
                    ans = ans+1
        return ans
