class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        cache[0] = 0

        def dfs(rem):
            if rem in cache: return cache[rem]
            if rem < 0: return amount + 1

            best = amount+1
            for coin in coins:
                best = min(best, 1 + dfs(rem - coin))

            cache[rem] = best
            return best
             
        x = dfs(amount)
        if dfs(amount) == amount + 1: return -1
        return x