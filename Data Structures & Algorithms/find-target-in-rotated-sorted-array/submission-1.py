class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < start:
                r = mid-1
            else:
                l = mid + 1
        
        if l > len(nums) - 1:
            l= start


        a = self.binarysearch(nums[0:l], target)
        b = self.binarysearch(nums[l:], target)
        print('asdfasdf')
        print(a,b)
        if a == -1 and b == -1:
            return -1
        if b != -1:
            return b + l
        return a

    def binarysearch(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        print(l, r, len(nums))
        if r == len(nums)-1 or r == 0:
            return -1
        return r