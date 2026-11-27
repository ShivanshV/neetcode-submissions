class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        minLeft = height[left]
        minRight = height[right]
        total = 0

        while left < right:
            if minLeft <= minRight:
                left+=1
                if height[left] <= minLeft:
                    total+=(minLeft - height[left])
                else:
                    minLeft = height[left]

            else:
                right-=1
                if height[right] <= minRight:
                    total+= (minRight - height[right])
                else:
                    minRight = height[right]
        
        return total

            


     