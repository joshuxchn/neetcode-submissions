class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) - 1

        x = []
        for key, val in count.items():
            x.append((val, key))

        heapq.heapify(x)
        time = 0

        #while there's still stuff in the heap or q
        q = deque()
        while x or q:
            time += 1

            #if there's stuff left in the heap
            if x:
                a, b = heapq.heappop(x)
                a += 1 #negative

                if a != 0:
                    q.append((a, time+n, b))

            # check if a cooling task is available again
            if q and q[0][1] == time:
                a, ready_time, b = q.popleft()
                heapq.heappush(x, (a, b))

        return time



