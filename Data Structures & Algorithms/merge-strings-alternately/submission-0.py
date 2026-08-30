class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word2) == 0:
            return word1
        
        res = ""
        i = 0
        while i < len(word1) and i<len(word2):
            res += word1[i] + word2[i]
            i+=1
        
        if len(word1) > len(word2):
            res += word1[i::]
        elif len(word2) > len(word1):
            res += word2[i::]

        return res