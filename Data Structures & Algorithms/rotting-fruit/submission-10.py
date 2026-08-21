class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #count how many fresh banans there are, tally
            #if fresh banaas is same after minute 0 to 1, return -1

        #tally of minutes

        
        #start at the rotten bananas
        #if fresh banana, mark as rotten
        #each queue iteration is another minute, until queue is empty
        #don't need visited set because marking as 2 is the same
            #is the answer -1? because we only end when the queue is empty, which is after the last banana if filled, which will call again     

        minutes = 0
        fresh = 0
        q = deque()
        ROW, COL = len(grid), len(grid[0])

        def rot(r, c):
            nonlocal fresh
            if min(r, c) < 0 or r==ROW or c==COL or grid[r][c] == 0 or grid[r][c] == 2:
                return

            grid[r][c] = 2 
            fresh -= 1
            #mark as rotten before to prevent adding same fresh fruit   multiple times
            q.append((r,c))
        for r in range(ROW):
            for c in range(COL):
                x = grid[r][c]
                if x == 1:
                    fresh += 1
                elif x == 2:
                    q.append((r, c))
        if fresh == 0: return 0
        if len(q) == 0: return -1 #no rotten oranges
        
        while q and fresh != 0:
            for i in range(len(q)):
                r, c = q.popleft()
                
                
                #we need set because we keep adding rotten bananas
                #but wont it stop once we hit fresh == 0?
                #also if it's 2 we don't append...
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)

            minutes += 1


        #if we can't find any more fresh bananas, they won't be added to q
        #so loop breaks. but if any remain, then its not possible
        if fresh > 0:
            return -1

        return minutes




