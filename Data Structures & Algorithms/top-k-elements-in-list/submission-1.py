class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq= defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        keys = sorted(freq.keys(), key = lambda num:freq[num],reverse=True)
        
        return keys[:k]
        