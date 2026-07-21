class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r = len(matrix) * len(matrix[0]) - 1
        
        while l <= r:
            mid = (l + r) //2
            y = mid // len(matrix[0]) #row
            x = mid % len(matrix[0]) #column
            
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False