class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, fr in count.items(): #tuple
            freq[-fr].append(num) #if two of same freq, gets appended in list
        
        result = []
        for x in freq:
            print(x)
            for y in x:
                result.append(y)
                if (len(result) == k):
                    return result
