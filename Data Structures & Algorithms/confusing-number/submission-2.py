class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid = {2, 3, 4, 5, 7}
        rev = 0
        original = n

        while n > 0:
            i = n % 10
            if i == 6:
                i = 9
            elif i == 9:
                i = 6
            rev = (10*rev) + i
            if i in invalid:
                return False

            n=n//10

        return not original == rev