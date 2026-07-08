class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}

        for i in range(len(nums1)):
            m[nums2[i]]=i
        
        result=[]
        for num in nums1:
            result.append(m[num])


        return result