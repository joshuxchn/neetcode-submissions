class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subset = []
        res = []
        left = right = 0
        def backtrack(left, right):
            if len(subset) == 2 * n:
                res.append("".join(subset.copy()))
                return
            
            if left < n:
                subset.append('(')
                left += 1
                backtrack(left, right)
                left -= 1
                subset.pop()

            if right < left:
                subset.append(')')
                right += 1
                backtrack(left, right)
                right -= 1
                subset.pop()

        backtrack(left, right)
        return res