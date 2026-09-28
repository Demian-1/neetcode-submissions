class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        myS = []
        for i, t in enumerate(temperatures): 
            while myS and t > myS[-1][0]:
                idx = myS[-1][1]
                res[idx] = i - idx
                myS.pop()
            myS.append([t, i])
        return res 
