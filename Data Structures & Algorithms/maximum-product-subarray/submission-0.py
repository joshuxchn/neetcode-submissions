class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0] #best result so far

        currMax = currMin = 1

        for num in nums:
            #temp
            oldMax = currMax

            #best max if we take
            currMax = max(num, currMax*num, currMin*num)
            currMin = min(num, oldMax*num, currMin*num)

            best = max(currMax, best)

        return best

        