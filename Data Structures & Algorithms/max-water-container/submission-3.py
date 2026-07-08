class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        tail = len(heights) -1
        head = 0
        for i in range(len(heights) -1):
            area = (tail - head) * min(heights[head], heights[tail])
            if area > max_area:
                max_area=area
            

            if heights[head] > heights[tail]:
                tail -= 1
            else:
                head += 1
        
        return max_area

            

        