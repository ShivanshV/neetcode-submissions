class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        present = set()
        for num in nums:
            present.add(num)
        
        longest = 0
        for num in present:
            curr = 0
            if num-1 not in present:
                temp = num
                while temp in present:
                    curr+=1
                    temp+=1
                longest = max(longest,curr)
        
        return longest
        