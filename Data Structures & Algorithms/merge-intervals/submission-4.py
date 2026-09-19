class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #overlap logic: a <= a0, b >= b0
            #take the bigger interval
        stack = []
        #sort initially, so we can prevent O(n) search
        intervals.sort()
        for interval in intervals:
            if stack and stack[-1][1] >= interval[0]:
                while stack and stack[-1][1] >= interval[0]:
                    lower = stack[-1][0]
                    upper = stack[-1][1]
                    stack.pop()
                    stack.append([min(lower, interval[0]), max(upper, interval[1])])
                    interval[0] = 1000000
                    
            else: stack.append(interval)

        return stack