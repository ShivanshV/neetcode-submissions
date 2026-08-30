class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            n = len(s)-1 - i
            temp = s[i]
            s[i] = s[n]
            s[n] = temp
        """
        Do not return anything, modify s in-place instead.
        """
        