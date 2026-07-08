class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for i, n in enumerate(nums):
            prod = prod * nums[i]
        
        final = [0] * len(nums)
        for i, n in enumerate(nums):
            if nums[i] == 0:
                prodx = 1
                for j, n in enumerate(nums):
                    if i != j:
                        prodx = prodx * nums[j]
                final[i] = prodx
            else:
                final[i] = int(prod / nums[i])
        
        return final
