class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        #heap + q

        #q wait time, if time = time pop from q

        h = []
        for i in range(len(servers)): heapq.heappush(h, (servers[i], i))

        waiting = []
        time = 0
        n = len(tasks)
        tasks = tasks[::-1]
        result = []
        while tasks:
            #check if available server
                #if available, pop task
                #add to queue
            #check if waiting q is ready to be popped

            while waiting and waiting[0][0] == time: 
                heapq.heappush(h, heapq.heappop(waiting)[1])
            

            while tasks and n-len(tasks) <= time and len(h) > 0:
                s = heapq.heappop(h)
                t = tasks.pop()
                heapq.heappush(waiting, (time + t, s))
                result.append(s[1])

            if not h: time = waiting[0][0]
            else: time += 1
            
        return result

    
    