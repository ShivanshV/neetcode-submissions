class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len( s1):
            return False
        
        if len(s2) == len(s1):
            return "".join(sorted(s1)) == "".join(sorted(s2))
        
        freq = [0] * 26
        for letter in s1:
            freq[ord(letter) - ord('a')]+=1
        
        left = 0
        right = 0
        freq2 = [0] * 26
        while right < len(s2):
            freq2[ord(s2[right]) - ord('a')]+=1
            if (right+1) - left > len(s1):
                freq2[ord(s2[left]) - ord('a')]-=1
                left+=1
            
            if (tuple(freq) == tuple(freq2)):
                return True
            
            
            right+=1
        return False