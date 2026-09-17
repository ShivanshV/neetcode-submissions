class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []
   

        def helper(index, total):
            if total == target :
                res.append(curr.copy())
                return
            if index >= len(candidates):
                return
            if total > target:
                return
            
          
            
            curr.append(candidates[index])
            helper(index+1, total + candidates[index])


            #in the exclude branch use a while loop to have you start at a new number so duplicate combos are not made
            curr.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index+=1
            helper(index+1, total)
        
        helper(0,0)

        return res
