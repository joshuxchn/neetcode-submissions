class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #thought process
        # turn to target
            #min of 4-0 or 10-4

        #have deadends in a set
        visit = set(deadends)
        
        if '0000' in deadends:
            return -1

        steps = 0
        q = deque()
        q.append('0000')

        while q:
            steps += 1
            for _ in range(len(q)):
                lock = q.popleft()

                #conversion
                for i in range(4):
                    for j in [1, -1]:
                        digit = str((int(lock[i]) + j)%10)
                        nextLock = lock[:i] + digit + lock[i+1:]
                        
                        
                        if nextLock in visit:
                            continue
                        if nextLock == target:
                            return steps
                        q.append(nextLock)
                        visit.add(nextLock)
        return -1