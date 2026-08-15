class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)
        def backtrack(subset, nums, pick):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    #take
                    subset.append(nums[i])
                    pick[i] = True
                    backtrack(subset, nums, pick)

                    #remove
                    subset.pop()
                    pick[i] = False
                
        backtrack([], nums, pick)
        return res