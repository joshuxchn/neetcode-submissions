class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = k % len(nums)
        temp = []
        temp[0:x]=nums[len(nums)-x:len(nums)]
        nums[x:len(nums)]=nums[0:len(nums)-x]
        nums[0:x]=temp

        