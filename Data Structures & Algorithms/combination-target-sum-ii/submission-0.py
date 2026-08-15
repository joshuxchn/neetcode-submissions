class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        s = 0
        result = []
        candidates = sorted(candidates)
        def dfs(i):
            nonlocal s
            #need this first because we are not checking after the calls below,
            #check on next call
            if s == target:
                result.append(subset.copy())
                return
            if i == len(candidates) or s > target:
                return

            subset.append(candidates[i])
            s += candidates[i]
            dfs(i + 1)

            subset.pop()
            s -= candidates[i]
            
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return result
        