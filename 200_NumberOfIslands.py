class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None or len(grid) == 0:
            return 0
        
        r = len(grid)
        c = len(grid[0])
        
        numIslands = 0
        
        # iterate over the matrix
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    numIslands += 1
                    self.sinkIsland(grid, i, j)
        
        return numIslands
    
    def sinkIsland(self, grid, i, j):
        # sink the entire island connected to i,j to prevent recounting
        
        # grid direction traveresed
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return
        
        # water found, island finished
        if grid[i][j] == "0":
            return
        
        # sink the land
        grid[i][j] = "0"
        
        # sink all neighbouring land, using DFS
        self.sinkIsland(grid, i - 1, j)
        self.sinkIsland(grid, i + 1, j)
        self.sinkIsland(grid, i, j - 1)
        self.sinkIsland(grid, i, j + 1)