class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]

                if stack: #checks if there is left
                    h = min(height[i], height[stack[-1]]) - mid
                    res += h * (i - stack[-1] - 1)
            stack.append(i)

        return res