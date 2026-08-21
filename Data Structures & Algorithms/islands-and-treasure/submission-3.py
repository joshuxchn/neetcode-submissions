class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set() #hold set of COORDS, not values
        q = deque()

        def addCell(r, c):
            if (min(r, c) < 0 or r >= len(grid) or c >= len(grid[0])
                or (r, c) in visited or grid[r][c] <= 0 #can't be 0 or -1
                ):
                return

            q.append((r, c))
            visited.add((r,c))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row, col))
                
        dist = 0
        while q:
            n = len(q)
            for i in range(n):
                row, col = q.popleft()
                grid[row][col] = dist

                addCell(row-1, col)
                addCell(row+1, col)
                addCell(row, col-1)
                addCell(row, col+1)

            dist += 1
        
