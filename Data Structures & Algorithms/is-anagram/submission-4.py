class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = {}
        tDict = {}

        for letterS, letterT in zip(s, t):
            sDict[letterS] = sDict.get(letterS, 0) + 1
            tDict[letterT] = tDict.get(letterT, 0) + 1
        
        for key, val in sDict.items():
            if key not in tDict:
                return False
            if sDict[key] != tDict[key]:
                return False
        
        return True
        
     



