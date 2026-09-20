class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def helper(op, closed):
            if len(curr) == n*2:
                res.append("".join(curr))
                return
            
            if op > 0:
                curr.append("(")
                helper(op-1,closed)
                curr.pop()
            if closed > op:
                curr.append(")")
                helper(op, closed-1)
                curr.pop()
        
        helper(n,n)

        return res

            
            