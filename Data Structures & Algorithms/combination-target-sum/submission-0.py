class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []
        def helper(index, total):
            if total == target:
                res.append(curr.copy())
                
                return
            if total > target or index >= len(nums):
                
                return
            
            total+=nums[index]
            curr.append(nums[index])
            helper(index,total)

            curr.pop()
            total-=nums[index]

            helper(index+1, total)
        
        helper(0,0)
        return res
