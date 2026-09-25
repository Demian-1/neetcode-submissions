class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1 
        maxA = 0
        """
        maxA = 1
        maxH = 24
        1,  7,  2,  5,  12, 3,  500,500,7,  8,  4,  7,  3,  6
                                l   r
        0   1   2   3   4   5   6   7   8   9   10  11  12  13
        """
        while l < r:
            maxA = max(maxA, min(heights[l], heights[r]) * (r - l)) 
            if heights[l] < heights[r]: 
                l += 1
            else:
                r -= 1
        return maxA
