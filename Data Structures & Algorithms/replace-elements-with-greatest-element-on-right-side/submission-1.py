class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx=arr[-1]
        arr[-1]=-1

        for i in reversed(range(len(arr)-1)):
            temp = arr[i]
            arr[i] = mx


            if temp > mx:
                mx=temp




        return arr