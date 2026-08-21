class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(row, col):
            if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) 
            or grid[row][col] == 0):
                return 0
            
            grid[row][col] = 0
            
            return 1 + (dfs(row + 1, col) + dfs(row - 1, col) +
                dfs(row, col + 1) + dfs(row, col-1)
                )

        
        res = 0
        for row in range(len(grid)):
            while 1 in grid[row]:
                print(row)
                res = max(res, dfs(row, grid[row].index(1)))
                
        
        return res