class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        
        for token in tokens:
            if token not in "+-*/":
                nums.append(int(token))
                
            else:
                num1 = nums.pop()
                num2 = nums.pop()

                if token == "+":
                    nums.append(num1+num2)
                elif token == "*":
                    nums.append(num1*num2)
                elif token == "/":
                        nums.append(int(num2/num1))
                elif token == "-":
                    nums.append(num2-num1)
           # print(nums) 
        
        return nums.pop()
                


