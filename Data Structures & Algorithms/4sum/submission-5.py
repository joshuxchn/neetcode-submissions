class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results=[]
        for head in range(len(nums) - 1):
            if head > 0 and nums[head] == nums[head - 1]:
                continue
            for head_two in range(head + 1, len(nums) - 1):
                if head_two > head + 1 and nums[head_two] == nums[head_two - 1]:
                    continue
                inner = head_two + 1
                tail = len(nums) - 1

                while inner < tail:
                    sum_ = nums[head] + nums[head_two] + nums[tail] + nums[inner]
                    if sum_ < target:
                        inner += 1
                    elif sum_ > target:
                        tail -= 1
                    else:
                        results.append([nums[head], nums[head_two], nums[inner], nums[tail]])
                        inner += 1
                        tail -= 1

                        while nums[inner - 1] == nums[inner] and inner < tail:
                            inner += 1
        
        return results


                
