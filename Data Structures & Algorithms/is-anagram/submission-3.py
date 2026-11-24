class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = defaultdict(int)
        tDict = defaultdict(int)

        for letterS, letterT in zip(s, t):
            sDict[letterS] += 1
            tDict[letterT] += 1
        
        for key, val in sDict.items():
            if key not in tDict:
                return False
            if sDict[key] != tDict[key]:
                return False
        
        return True
        
     



