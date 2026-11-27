class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        for i in range(len(position)):
            pairs.append((position[i],speed[i]))
        
        pairs.sort()

        for pair in pairs:
            pos, speed = pair
            time = (target-pos)/speed
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        

        #print(pairs)
        return len(stack)