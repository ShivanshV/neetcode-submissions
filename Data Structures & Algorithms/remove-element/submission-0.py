class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                j = i + 1
                while j < len(nums):
                    if nums[j] != val:
                        #swap
                        nums[i] = nums[j]
                        nums[j] = val
                        k+=1
                        break
                    j+=1
            else:
                k+=1
        return k
