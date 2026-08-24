class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)
        while len(stones) >= 2:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -abs(y-x))
        if len(stones) == 1: return -heapq.heappop(stones)
        return 0
        