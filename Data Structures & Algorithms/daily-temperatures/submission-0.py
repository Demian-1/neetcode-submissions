class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
                                i
        30, 38, 30, 36, 35, 40, 28
    res 1   4    1   2   1
        0   1   2   3   4   5   6
        40:5, 28:6          

        """
        res = [0]*len(temperatures)
        myS = []
        for i, t in enumerate(temperatures): 
            while myS and t > myS[-1][0]:
                idx = myS[-1][1]
                res[idx] = i - idx
                myS.pop()
            myS.append([t, i])
        return res 
