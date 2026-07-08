class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        if len(nums)==1:
            return nums[0]
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                return nums[i]
            if nums[i] != nums[i+1]:
                return nums[i]
 

        return -1

