class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        curr = s[left]
        temp = {}
        longest = 0
        maxFreq = 0
        while right < len(s):
            temp[s[right]] = temp.get(s[right], 0) + 1
            maxFreq = max(maxFreq, temp[s[right]])

            while (right+1 - left) - maxFreq > k:
                temp[s[left]]-=1
                left+=1
            
            longest = max(longest, (right+1 - left))
            right+=1
        return longest

        