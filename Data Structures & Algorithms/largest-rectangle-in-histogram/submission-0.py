class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        widths = [0] * len(heights)
        stack=[]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                widths[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

            while stack and i==len(heights)-1:
                widths[stack[-1]] = 1+i - stack[-1]
                stack.pop()
            
        
        stack.clear()
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                widths[stack[-1]] += stack[-1] - i - 1 #already counted itself last turn
                stack.pop()
            stack.append(i)

            while stack and i==0:
                widths[stack[-1]] += stack[-1]-i
                stack.pop()
              
        
        mx=0
        for i in range(len(widths)):
            if heights[i] * widths[i] > mx:
                mx = heights[i] * widths[i]
        return mx