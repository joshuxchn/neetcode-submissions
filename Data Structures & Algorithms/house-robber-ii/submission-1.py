class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * (len(nums) - 1)
        #edge case 1: rob end, can't rob start
        #edge case 2: rob start, can't rob end
        #conclusion: pick one of the two
        
        one = nums[1:]
        two = nums[:len(nums)-1]
        if len(nums) == 1:
            return nums[0]

        def dfs(i, arr):
            if i >= len(arr):
                return 0
            if cache[i] != -1: return cache[i]

            cache[i] = max(arr[i] + dfs(i + 2, arr), dfs(i+1, arr))
            return cache[i]
        one = dfs(0, one)
        cache = [-1] * len(nums)
        two = dfs(0, two)
        
        return max(one, two)


        



