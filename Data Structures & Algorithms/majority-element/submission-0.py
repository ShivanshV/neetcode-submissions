class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        res = 0
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
            if freq.get(nums[i]) > res:
                maxNum = nums[i] 
                res = freq.get(nums[i])
        return maxNum 
