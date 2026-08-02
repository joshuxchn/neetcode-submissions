class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        print(nums)
        l = count = 0
        s = 0
        for r in range(len(nums)):
            s += nums[r]


            while ((r - l + 1) * nums[l]) - s > k:
                s -= nums[l]
                l += 1
            
            count = max(count, r - l + 1)
        return count