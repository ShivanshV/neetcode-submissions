class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [-1] * N

       

        def decode(i):
            if i >= N:
                return 1
            if s[i] == "0":
                return 0
            
            if dp[i] != -1:
                return dp[i]

            dp[i] = decode(i+1)

            if (s[i] == "1" or s[i] == "2") and i < N-1:
                num = int(s[i:i+2])
                if  num >= 1 and num <= 26:
                    dp[i]+= decode(i+2)
                
            return dp[i]

        return decode(0)