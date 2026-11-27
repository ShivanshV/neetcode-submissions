class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        longest = 0
        seen = defaultdict(int)
        while end < len(s):
            letter = s[end]
            if letter in seen and seen[letter] != -1:
                while start <= seen[letter]:
                    seen[s[start]] = -1
                    start+=1
            else:
                longest = max(longest, (end+1)-start)
                print(f"{longest} {s[start:end+1]}")
            seen[letter] = end
            end+=1

        return longest

