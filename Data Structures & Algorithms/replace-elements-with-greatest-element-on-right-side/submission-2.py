class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx=arr[-1]
        ans=[0] * len(arr)
        ans[-1]=-1
        for i in reversed(range(len(arr)-1)):
            ans[i] = mx

            if arr[i] > mx:
                mx=arr[i]




        return ans