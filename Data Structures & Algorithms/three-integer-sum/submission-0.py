class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        head = 0
        tail = len(nums) - 1
        inner = 1
        out = []
        for head in range(len(nums) - 1):
            inner = head+1
            tail = len(nums) - 1
            while not inner == tail:
                sum = nums[head] + nums[tail] + nums[inner]
                if (sum < 0):
                    inner += 1
                elif (sum > 0):
                    tail -= 1                      
                elif sum==0:
                    if [nums[head], nums[inner], nums[tail]] in out:
                        inner += 1
                        continue
                    out.append([nums[head], nums[inner], nums[tail]])
                    inner += 1




        return out
