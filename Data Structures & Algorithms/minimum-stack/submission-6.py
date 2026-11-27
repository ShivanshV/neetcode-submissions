class MinStack:

    def __init__(self):
       
       self.minimum = float('inf') 
       self.array = []

    def push(self, val: int) -> None:
        if val < self.minimum:
            self.minimum = val

        self.array.append((val, self.minimum))
       

        

    def pop(self) -> None:
        self.array.pop()
        self.minimum = self.getMin()

    def top(self) -> int:
        return self.array[-1][0]

    def getMin(self) -> int:
        if self.array:
            return self.array[-1][1]
        else:
            return float('inf') 
