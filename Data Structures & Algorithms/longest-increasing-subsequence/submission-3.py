class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def helper(index, prev):
            if index == len(nums):
                return 0
            
            state = (index, prev)
            if state in memo:
                return memo[state]
            
            res = helper(index+1, prev)
            if prev == -1 or nums[index] > nums[prev]:
                res = max(res, 1 + helper(index+1, index))
            memo[state] = res
            return res
        
        return helper(0,-1)