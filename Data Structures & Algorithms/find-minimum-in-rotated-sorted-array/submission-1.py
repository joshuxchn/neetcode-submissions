class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < start:
                r = mid-1
            else:
                l = mid + 1
        if l > len(nums) - 1:
            return start
        return nums[l]