class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxL = height[l]
        maxR = height[r]
       
        
        
        filled = 0
        temp = 0
        
        while l < r:
            if maxL < maxR:
                filled += min(maxL,maxR) - height[l]
                l+=1
                maxL = max(maxL,height[l])
            else:
                filled+= min(maxL,maxR) - height[r]
                r-=1
                maxR = max(maxR,height[r])
           
        return filled
