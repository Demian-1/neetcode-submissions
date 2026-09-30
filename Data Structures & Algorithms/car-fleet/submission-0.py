class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        time = [0] * len(position)
        res = 1
        i = 0

        while(i < len(position)):
            time[i] = (position[i], (target - position[i]) / speed[i])
            i+=1
        
        # Sort list of time by corresponding position
        time.sort(key=lambda x: x[0], reverse = True)

        j = 1
        currMin = time[0][1]
        while(j < len(position)):
            if time[j][1] > currMin:
                res += 1
                currMin = time[j][1]
            
            j+=1
        return res