class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}
        for i in range(len(keyboard)):
            d[keyboard[i]]=i
        
        res=0
        print(d)
        for i in range(len(word)):
            if i == 0:
                res+=d[word[i]]
            else:
                res+= abs(d[word[i]]-d[word[i-1]])
            
            print(i, res)

        return res