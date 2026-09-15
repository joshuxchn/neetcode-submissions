class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #memo the minimum # of coins at X amount remaining
        cache = [amount+1] * (amount + 1)
        coins.sort()

        if amount == 0: return 0
        if amount < coins[0]: return -1
        cache[coins[0]] = 1
        cache[0] = 0

        #i is the remaining amount
        for i in range(coins[0], amount + 1):
            for coin in coins:
                remaining = i - coin
                if remaining < 0: continue

                cache[i] = min(cache[i], 1 + cache[remaining])
        
        if cache[amount] == amount + 1:
            print("taken")
            return -1
        return cache[amount]
#cache
#0 - 0
# 1 : 1
# 2: 2
# 5 : 1
#