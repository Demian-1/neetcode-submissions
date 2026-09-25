class Solution:
    def trap(self, height: List[int]) -> int:
        """
        0,  2,  0,  3,  1,  0,  1,  3,  2,  1
maxL    0   0   2   2   3   3   3   3   3   3
maxR    3   3   3   3   3   3   3   2   1   0
water   0   0   2   0   2   3   2   0   0   0
        """
        maxL = [0] * len(height)
        maxL[0] = height[0]
        maxR = [0] * len(height)
        maxR[len(height) - 1] = height[len(height) - 1]
        for i, h in enumerate(height): 
            if i > 0:
                maxL[i] = max(maxL[i-1], h)

        #print('MaxL: ' + str(maxL))
        
        for i, h in reversed(list(enumerate(height))):
            if i < len(height)-1:
                maxR[i] = max(maxR[i+1], h)

        #print('MaxR: ' + str(maxR))
        totalWater = 0 
        for i, h in enumerate(height):
            if i == 0 or i == len(height) - 1:
                continue
            minMaxHeight = min(maxL[i-1], maxR[i+1])
            currWater = minMaxHeight - h
            if currWater > 0: 
                totalWater += currWater
            
        return totalWater
