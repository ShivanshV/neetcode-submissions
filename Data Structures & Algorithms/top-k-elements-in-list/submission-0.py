class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        freqList = []
        for key, val in freq.items():
            freqList.append((-val,key))
        
        heapq.heapify(freqList)
        topk = []
        for i in range(k):
            topk.append(heapq.heappop(freqList)[1])
        
        return topk
