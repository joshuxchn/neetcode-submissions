class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if k == 0:
            return False
        
        L = 0
        window = set()
        for i in range(len(nums)):
            
            if i - L > k:
                window.remove(nums[L]) #remove oldest
                L += 1
            if nums[i] in window:
                return True
            
            window.add(nums[i])


        return False

