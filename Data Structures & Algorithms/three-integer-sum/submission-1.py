# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         results=[]
#         for head in range(len(nums) - 1):
#             tail = len(nums) - 1
#             inner = head + 1
#             while inner < tail:
#                 sum = nums[head] + nums[inner] + nums[tail]
#                 if sum > 0:
#                     tail -= 1
#                 elif sum < 0:
#                     inner += 1
#                 if sum == 0:
#                     results.append([nums[head], nums[inner], nums[tail]])
#                     tail -= 1
#                     inner += 1
        
#         return results
                
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        head = 0
        tail = len(nums) - 1
        inner = 1
        out = set()

        while head < inner < tail:
            total = nums[head] + nums[inner] + nums[tail]

            if total < 0:
                inner += 1
            elif total > 0:
                tail -= 1
            else:
                out.add((nums[head], nums[inner], nums[tail]))
                inner += 1

            # collision: inner met tail, advance head
            if inner >= tail:
                head += 1
                inner = head + 1
                tail = len(nums) - 1

        return [list(t) for t in out]