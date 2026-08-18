class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        pq, aq = deque(), deque()

        def bfs(q, visited):
            while q:
                r, c = q.popleft()

                directions = [
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1)
                ]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # stay inside grid
                    if nr < 0 or nr >= len(heights) or nc < 0 or nc >= len(heights[0]):
                        continue

                    # already visited
                    if (nr, nc) in visited:
                        continue

                    # reverse flow:
                    # can only go to equal/higher cells
                    if heights[nr][nc] < heights[r][c]:
                        continue

                    q.append((nr, nc))
                    visited.add((nr, nc))
    
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if row == 0 or col == 0 :
                    pq.append((row, col))
                    pacific.add((row, col))
                if row == len(heights) - 1 or col == len(heights[0]) - 1:
                    aq.append((row, col))
                    atlantic.add((row, col))
        
        bfs(pq, pacific)
        bfs(aq, atlantic)
        
        result = []
        for r, c in pacific:
            if (r, c) in atlantic:
                result.append([r, c])
        return result
    
