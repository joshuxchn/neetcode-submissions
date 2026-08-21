class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        #checks cells that reach respective sets
        reached_pac = set()
        reached_alt = set()
        pac_q = deque()
        alt_q = deque()


        #why reverse: we can guarentee that neighbor cells are in (if valid)
        def bfs(q, s):

            #helper function to check edge cases
            def addCell(original, r, c):
                if (min(r, c) < 0 or r >= len(heights) or c >= len(heights[0])
                    or (r, c) in s):
                    return

                #reverse flow
                if original > heights[r][c]:
                    return

                q.append((r, c))
                s.add((r,c))

            while q:
                r, c = q.popleft()
                original = heights[r][c]

                addCell(original, r+1, c)
                addCell(original, r-1, c)
                addCell(original, r, c+1)
                addCell(original, r, c-1)

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if row == 0 or col == 0:
                    pac_q.append((row,col))
                    reached_pac.add((row,col))
                if row == len(heights) - 1 or col == len(heights[0]) - 1:
                    alt_q.append((row, col))
                    reached_alt.add((row,col))
        
        print(reached_alt & reached_alt)
        bfs(pac_q, reached_pac)
        bfs(alt_q, reached_alt)

        return list(reached_alt & reached_pac)
