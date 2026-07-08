class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        head = 1
        tail = len(nums)
        for i in range(len(nums)):
            if nums[head - 1] + nums[tail - 1] == target:
                return [head, tail]
            if nums[head - 1] + nums[tail - 1] > target:
                tail -= 1
            else:
                head += 1