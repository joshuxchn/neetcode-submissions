class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n=len(nums)
        for left in range(n - 1):
            #duplicate check
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            

            mid = left + 1
            right = n - 1
            while mid < right:
                s = nums[left]+nums[mid]+nums[right]
                if s > 0: right -= 1
                elif s < 0: mid += 1
                else: 
                    result.append([nums[left],nums[mid],nums[right]])
                    right -= 1
                    mid += 1

                    while mid < right and nums[right] == nums[right + 1]: 
                        #needs to be right+1 because i adjusted right right before this lmao
                        right -= 1

        return result

    #0111234556