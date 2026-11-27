class MinStack:

    def __init__(self):
       self.index = -1
       self.minimum = float('inf') 
       self.array = []

    def push(self, val: int) -> None:
        if val < self.minimum:
            self.minimum = val

        self.array.append((val, self.minimum))
        self.index+=1

        

    def pop(self) -> None:
        self.array.pop()
        
        self.index-=1
        self.minimum = self.getMin()

    def top(self) -> int:
        return self.array[self.index][0]

    def getMin(self) -> int:
        if self.array:
            return self.array[self.index][1]
        else:
            return float('inf') 
