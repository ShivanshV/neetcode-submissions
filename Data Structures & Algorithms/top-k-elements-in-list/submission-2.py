class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        heap = []
        res = []

        for num in nums:
            freq[num] += 1
        
        for key, val in freq.items():
            print(key,val)
            heap.append((-val,key))
        
        heapq.heapify(heap)
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
