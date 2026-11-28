class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for letter in t:
            freq[letter] = freq.get(letter, 0 ) + 1
        
        left = -1 
        
        matches = 0

        freq2 = {}

        for i in range(len(s)):
            if s[i] in freq:
                left = i
                break;
        print(freq)
        print(left)
        
        if left == -1:
            return ""
        matches = 0
        right = left
        shortestLeft = 0
        shortestRight = 0
        while right < len(s):
           
            freq2[s[right]] = freq2.get(s[right], 0) + 1
            if s[right] in freq and freq2[s[right]] == freq[s[right]]:
                matches += 1
                
            
            while matches == len(freq):
               # print(f"{left} {right} {s[left:right+1]} okay")
                if shortestRight==shortestLeft or right+1 - left < (shortestRight - shortestLeft):
                    shortestLeft = left
                    shortestRight = right+1 #when returning add 1 to right
                   # print(s[shortestLeft:shortestRight])
                #print(s[left])
                freq2[s[left]]-= 1
                if s[left] in freq and freq2[s[left]] < freq[s[left]]:
                    matches-=1
                left+=1
                #print(freq2)
                
                #print(f"{left} {right}")
                
            right+=1
        
        return s[shortestLeft:shortestRight]


            