class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l , r = 0, 0
        while r < len(nums):
            if nums[r] == nums[l]:
                r+=1
                continue
            else:
                l+=1
                nums[l] = nums[r]
        
        return l+1
