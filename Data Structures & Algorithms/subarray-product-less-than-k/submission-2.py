class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = count = 0

        if k == 0:
            return 0
    
        prod = 1
        for r in range(len(nums)):
            prod *= nums[r]
            while prod >= k and l < r:
                prod = prod // nums[l]
                l += 1

            if prod < k:
                count += r - l + 1
            
            # print(count, nums[l:r+1])
        return count

            