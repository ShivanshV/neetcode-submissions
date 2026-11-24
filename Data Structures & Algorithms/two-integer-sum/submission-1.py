class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {} #target number: prev index
        for i in range(len(nums)):
            if nums[i] in pairs:
                return [pairs.get(nums[i]), i]
            pairs[target-nums[i]] = i
        
        return -1
    