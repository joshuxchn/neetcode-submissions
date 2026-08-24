from _heapq import heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x,y in points:
            distance = math.sqrt((x)**2 + (y)**2)
            distances.append([distance, [x,y]])

        
        heapq.heapify(distances)
        result = []

        for i in range(k):
            result.append(heapq.heappop(distances)[1])

        return result
        
