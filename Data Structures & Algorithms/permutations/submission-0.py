class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
            
        prev = self.permute(nums[1:])
        temp = []
        for p in prev:
            for i in range(len(p)+1):
                pcopy = p.copy()
                pcopy.insert(i,nums[0])
                temp.append(pcopy)
            
        return temp
        

