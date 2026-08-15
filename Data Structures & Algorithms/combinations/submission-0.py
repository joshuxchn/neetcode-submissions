class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        subset = []
        result = []
        def dfs(i):
            print(subset)
            if len(subset) == k:
                result.append(subset.copy())
                return
            if i == n:
                return

            subset.append(i + 1)
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result