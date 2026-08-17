class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [-1] * len(coins)
        for i in range(len(cache)):
            cache[i] = [-1] * (amount + 1)

        def dfs(i, amnt):
            if amnt == 0:
                return 0
            
            if i == len(coins) or amnt < 0:
                return float("inf")
            
            if cache[i][amnt] != -1: return cache[i][amnt]

            #take, stay on same or #don't take, call next
            cache[i][amnt] = min(1 + dfs(i, amnt - coins[i]), dfs(i + 1, amnt))
            return cache[i][amnt]

        res = dfs(0, amount)
        if res == float("inf"): return -1
        return res