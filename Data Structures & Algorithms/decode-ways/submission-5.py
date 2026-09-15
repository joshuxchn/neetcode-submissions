class Solution:
    def numDecodings(self, s: str) -> int:
        second_digits = set({'0', '1', '2', '3', '4', '5', '6'})
        cache = {} #stores numDecoding of substring
        n = len(s)

        def dfs(i): #substring index i to end
            if i == n: return 1
            if s[i] == '0': return 0 #this needs to negate the whole tally
            if s[i:n] in cache: return cache[s[i:n]]
            
            cache[s[i:n]] = dfs(i+1) #take
            if i + 1 < n and s[i] in "12":
                if (s[i]=='1' or s[i+1] in second_digits):
                    cache[s[i:n]] += dfs(i + 2) #take two digit

            return cache[s[i:n]]

        return dfs(0)