class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        picked = [False] * len(nums)
        nums.sort()
        def backtrack(subset, nums, picked):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if not picked[i]:
                    if i > 0 and nums[i] == nums[i - 1] and picked[i - 1]:
                        continue
                    picked[i] = True
                    subset.append(nums[i])
                    backtrack(subset, nums, picked)
                    subset.pop()
                    picked[i] = False
        
        backtrack([], nums, picked)
        return res

      
