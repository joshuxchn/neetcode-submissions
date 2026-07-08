class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            x = sorted(s)
            if str(x) in d:
                d[str(x)].append(s)
            else:
                d[str(x)]=[s]
        
        result = []
        for di in d:
            result.append(d[di])
        return result


        