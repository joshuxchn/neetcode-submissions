class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
            l= start


        b = self.binarysearch(nums[l:], target)
        if b != -1:
            return b + l
        return self.binarysearch(nums[0:l], target)

    def binarysearch(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return -1