class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1  ,2  ,4  ,6]
    1   [1  ,2  ,8  ,48]
        [48 ,48 ,24 ,6] 1
        [48 ,24 ,12 ,8]


        [-1 ,0  ,1  ,2  ,3]
    1   [-1 ,0  ,0  ,0  ,0]
        [0  ,0  ,6  ,6  ,3] 1
        [0  ,-6 ,0  ,0  ,0]
        """
        n = len(nums);
        pref = [1] * n
        suff = [1] * n
        res = [1] * n
        for i in range(n):
            if i == 0:
                pref[i] = nums[i]
            else:
                pref[i] = pref[i-1]*nums[i]
        
        for i in reversed(range(n)):
            if i == n - 1:
                suff[i] = nums[i]
            else:
                suff[i] = nums[i] * suff[i+1]

        for i in range(n):
            if i == 0:
                res[i] = suff[i+1]
            elif i == n - 1:
                res[i] = pref[i-1]
            else:
                res[i] = pref[i-1] * suff[i+1]

        return res