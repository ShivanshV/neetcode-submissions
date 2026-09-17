class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = []
        curr = []
        valid = set()
        def helper(index):
          
            if index == len(nums):
                temp.append(curr.copy())
                return
            curr.append(nums[index])
            helper(index+1)
            curr.pop()
            helper(index+1)
            
            
            

        helper(0)
        print(temp)
        return temp