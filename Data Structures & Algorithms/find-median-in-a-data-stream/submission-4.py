from _heapq import heapify
class MedianFinder:

    def __init__(self):
        #min, max heap
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)

        self.median = 0
        

    def addNum(self, num: int) -> None:
        #if greater than current median, add to right side. else left side
        #recalculate total size, the the size with more elements should have the new median
        #if the size is equal, the new median is the
        if (num) < self.median:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        
        #balance too many on left side
        while len(self.left) - len(self.right) > 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        
        while len(self.right) - len(self.left) > 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))

        #odd, take first element of side with more
        if (len(self.left) + len(self.right)) % 2 != 0:
            if len(self.left) > len(self.right):
                self.median = -self.left[0]
            else:
                self.median = self.right[0]
        else: #even, take average of both firsts
            if len(self.right) == 0: return
            self.median = float(self.right[0] - self.left[0]) / 2

        

    def findMedian(self) -> float:
        return float(self.median)
        