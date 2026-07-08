class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            mx = 0
            for j in range(i+1, len(arr)):
                if arr[j] > mx:
                    mx = arr[j]
        
            arr[i] = mx

        arr[-1]=-1
        return arr