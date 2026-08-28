class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        streak = 0
        for n in nums:
            if n == 1:
                streak += 1
                best = max(streak, best)
            else:
                best = max(streak, best)
                streak = 0

        return best