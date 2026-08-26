class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        #this stores the LIS from index i to the end
        cache = {}

        def dfs(i, prev):
            if i >= len(nums): return 0
            if (i, prev) in cache: return cache[(i, prev)]

            skip = dfs(i + 1, prev) #move to next, don't change prev
            take = 0
            if prev < nums[i]:
                take = 1 + dfs(i + 1, nums[i])
            cache[(i, prev)] = max(take, skip)

            return cache[(i, prev)]
        
        return dfs(0, -1001)

        #if the number is less than the last number, add it, dfs
        #if greater, either take and reset LIS to 0 or skip. take the max of the two
        