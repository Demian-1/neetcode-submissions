class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxL[0] = height[0]
        maxR = [0] * len(height)
        maxR[-1] = height[-1]
        
        for i, h in enumerate(height): 
            if i > 0:
                maxL[i] = max(maxL[i-1], h)
        
        for i, h in reversed(list(enumerate(height))):
            if i < len(height)-1:
                maxR[i] = max(maxR[i+1], h)

        totalWater = 0 
        for i, h in enumerate(height):
            if i == 0 or i == len(height) - 1:
                continue
            minMaxHeight = min(maxL[i-1], maxR[i+1])
            currWater = minMaxHeight - h
            if currWater > 0: 
                totalWater += currWater
            
        return totalWater
