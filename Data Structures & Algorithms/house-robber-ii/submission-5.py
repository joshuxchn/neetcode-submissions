class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_two(nums[1:]), self.rob_two(nums[:-1]))

    def rob_two(self, nums: List[int]) -> int:
        cache = [-1] * (len(nums))

        cache[0] = nums[0]
        if len(nums) == 1: return nums[0]
        cache[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            #a: rob now, also robbed 2 prior
            #b: rob now, didn't rob prior
            cache[i] = max(nums[i] + cache[i-2], cache[i-1])

        return cache[len(nums)-1]