class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums) < 3:
            return []

        left = 0
        mid = left + 1
        right = len(nums) - 1
        res = []

        

        while left < len(nums) - 2:
            if left > 0 and nums[left] == nums[left-1]:
                left+=1
                continue

            mid = left+1
            right = len(nums)-1

            # if left > 0 and nums[left] == nums[left-1]
            while mid < right:
                
                if nums[left] + nums[mid] + nums[right] > 0:
                    right-=1
                  #  print("more")
                elif nums[left] + nums[mid] + nums[right] < 0:
                    mid+=1
                   # print("less")
                else:
                   # print("equal")
                    res.append([nums[left],nums[mid],nums[right]])
                    mid += 1
                    while mid < right and nums[mid] == nums[mid-1]:
                        mid+=1
        
            left+=1
        
        return res
                    

    