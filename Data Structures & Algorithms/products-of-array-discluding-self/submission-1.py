class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = 1
        res = [1] * (len(nums))
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        
        return res


