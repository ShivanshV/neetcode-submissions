class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(op, closed, curr):
            if len(curr) == n*2:
                res.append(curr)
                return
            
            if op > 0:
                helper(op-1,closed, curr + "(")
            if closed > op:
                helper(op, closed-1, curr + ")")
        
        helper(n,n,"")

        return res

            
            