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
            mid = (l+r)//2
            print(l, r, mid)
            if mid - l + 1 != r - mid:
                print('taken')
                x = reader.compareSub(l, mid - 1, mid + 1, r)
                print(x)
            else:
                x = reader.compareSub(l, mid, mid + 1, r)
                print(x)
            if x == 0:
                return mid
            elif x == -1:
                l = mid + 1 
            else:
                r = mid
        
        return l