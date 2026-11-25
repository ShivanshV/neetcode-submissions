class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1] * len(nums)
        backward = [1] * len(nums)

        for i in range(1, len(forward)):
            forward[i] = forward[i-1] * nums[i-1]
        
        for i in range(len(backward)-2, -1, -1):
            backward[i] = backward[i+1] * nums[i+1]
    

        res = []

        for i in range(len(nums)):
            res.append(forward[i]*backward[i])
        return res
