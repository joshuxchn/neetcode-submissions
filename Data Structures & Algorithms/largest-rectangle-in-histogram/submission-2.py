class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mx=0
        stack=[]
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                width=0
                h = heights[stack.pop()]
                if not stack:
                    width=i
                else:
                    width=i-stack[-1]-1
                mx = max(mx, width * h)
                
            stack.append(i)

        return mx