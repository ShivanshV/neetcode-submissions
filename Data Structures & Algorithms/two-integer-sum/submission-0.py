class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = defaultdict(int)
        #key stores target - num value stores index of current num

        for i in range(len(nums)):
            if nums[i] in pairs:
                return [pairs[nums[i]], i]
            pairs[target-nums[i]] = i
        return[-1,-1]