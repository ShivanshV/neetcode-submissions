class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def valid(s: str):
            open = []
            for c in s:
                if c == '(':
                    open.append('(')
                else:
                    if len(open) == 0:
                        return False
                    open.pop()
            if len(open) != 0:
                return False
            return True

        def helper(s: str):
            if len(s) == n * 2:
                if valid(s):
                    res.append(s)
                return
            helper(s + '(')
            helper(s + ')')
            
        helper("")
        return res