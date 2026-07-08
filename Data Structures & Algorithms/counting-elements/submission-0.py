class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        tally = 0
        for i in arr:
            if i + 1 in s:
                tally += 1
        
        return tally