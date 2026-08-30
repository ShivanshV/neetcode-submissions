class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-1, 1, -1):
            if i != len(nums)-1 and nums[i] == nums[i+1]:
                continue
            left = 0
            right = i-1
            while left < right:
                if nums[left]+nums[right] > -nums[i]:
                    right-=1
                elif nums[left]+nums[right] < -nums[i]:
                    left+=1
                else:
                    res.append([nums[left],nums[right],nums[i]])
                    lNum= nums[left]
                    while nums[left] == lNum and left < right:
                        left+=1
                    
                    
       
        return res
