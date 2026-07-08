class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        d = defaultdict(set)
        for a, b in similarPairs:
            d[a].add(b)
            d[b].add(a)
        
        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i] and sentence1[i] not in d[sentence2[i]]:
                return False
        
        return True
