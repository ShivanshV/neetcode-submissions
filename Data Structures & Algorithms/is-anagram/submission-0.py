class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = {}
        for c in s:
            if freq.get(c) == None:
                freq[c] = 1
            else:
                freq[c] +=1 
        
        for c in t:
            if freq.get(c) == None: 
                return False
            else:
                freq[c] -= 1
        
        for keys in freq.keys():
            if freq[keys] != 0:
                return False
        return True