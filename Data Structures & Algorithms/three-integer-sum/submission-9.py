class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left = 0
        res = []
        print(nums)
        while nums[left] <= 0 and left < len(nums)-2:
            if left > 0 and nums[left] == nums[left-1]:
                left+=1
                continue
            mid = left + 1
            right = len(nums)- 1
            while mid < right:
                temp = nums[left] + nums[mid] + nums[right]
                if temp == 0:
                    res.append([nums[left],nums[mid],nums[right]])
                    mid+=1
                    right-=1

                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                   
                    while mid < right and nums[right] == nums[right + 1]:
                        right -= 1 
                elif temp < 0:
                    mid+=1
                else:
                    right-=1
            left+=1
        return res