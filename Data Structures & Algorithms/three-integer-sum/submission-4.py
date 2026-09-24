class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        nums.sort()
        i = 0
        """

        -1  -2  1   2
            i   l   r

        t =  2
        
        """
        while i < len(nums): 
            curr = nums[i]
            if curr > 0: 
                break
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = curr + nums[l] + nums[r]
                if total < 0: 
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([curr, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                    r -= 1
                    while nums[r] == nums[r+1] and l<r:
                        r -= 1
            while i < len(nums) and curr == nums[i]:  
                i += 1
            
        return res    
            
                
                