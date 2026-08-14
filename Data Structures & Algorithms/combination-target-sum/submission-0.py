class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        s = 0
        def dfs(i):
            nonlocal s
            if s == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or s > target:
                return

            
            #case 1: try the same number
            subset.append(nums[i])
            s += nums[i]
            dfs(i)

            #case 3: skip current, try next number
            subset.pop()
            s -= nums[i]
            dfs(i + 1)

        dfs(0)
        return res