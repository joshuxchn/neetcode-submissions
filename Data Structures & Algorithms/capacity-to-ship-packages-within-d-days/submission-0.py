class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l <= r:
            mid = (l+r)//2
            if self.time_to_empty(weights, mid) > days:
                l = mid + 1 #need more capacity
            else:
                r = mid - 1
        return l

    def time_to_empty(self, weights, capacity):
        stack = weights[::-1]
        days=1
        tally = 0
        while stack:
            if stack[-1] + tally > capacity:
                tally = 0
                days += 1
            else:
                tally += stack.pop()
        return days