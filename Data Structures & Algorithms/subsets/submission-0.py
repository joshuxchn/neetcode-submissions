class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            #case 1: include number
            subset.append(nums[i])
            dfs(i + 1)

            #case 2: don't include
            subset.pop()
            dfs(i + 1)
            
        dfs(0)
        return res