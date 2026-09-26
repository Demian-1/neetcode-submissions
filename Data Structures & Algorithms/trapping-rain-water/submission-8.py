class Solution:
    def trap(self, height: List[int]) -> int:
        """
        mL = 3
        mR = 3
        tW = 9
        0,  2,  0,  3,  1,  0,  1,  3,  2,  1
                                    l
                                    r
        """
        l, r = 0, len(height) - 1
        mL, mR = height[l], height[r]
        tW = 0
        while l < r:
            if mL <= mR:
                tW += mL - height[l]
                l += 1
                mL = max(mL, height[l])
            else:
                tW += mR - height[r]
                r -= 1
                mR = max(mR, height[r])
        
        return tW

