# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        l = 0
        r = reader.length() - 1

        while l < r:
            mid = (l + r) //2
            x = 0
            if l == r:
                return mid
            if mid - l + 1 != r - mid:
                x = reader.compareSub(l, mid - 1, mid + 1, r)
            else:
                x = reader.compareSub(l, mid, mid + 1, r)
            if x == 0:
                return mid #both sides are even, so middle must be peak
            elif x == 1:
                r = mid
            else:
                l = mid + 1
        
        return l