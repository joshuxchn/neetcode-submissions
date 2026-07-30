class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = count = 0
        s=0
        for r in range(len(arr)):
            s += arr[r]
            while r - l + 1 > k:
                s -= arr[l]
                l += 1

            avg = s / k
            if avg >= threshold and r - l + 1 == k:
                count += 1
            
        return count 
