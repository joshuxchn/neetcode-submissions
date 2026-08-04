class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1

        while r - l + 1 > k:
            l_diff = abs(arr[l] - x)
            r_diff  = abs(arr[r] - x)
            if l_diff > r_diff:
                l += 1
            else:
                r -= 1
        
        return arr[l:r+1]