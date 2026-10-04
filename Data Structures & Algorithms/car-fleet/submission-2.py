class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """

        0   1   2   3   4   5   6   7   8   9   10

        1   2           2           1


        """

        cars = []
        for i, p in enumerate(position): 
            cars.append([p,speed[i]])

        cars.sort(key = lambda c: c[0])
        fleets = [] 
        for i in range(len(cars) - 1, -1, -1):
            t = (target - cars[i][0]) / cars[i][1]
            if not fleets: 
                fleets.append(t)
            if fleets[-1] < t:
                fleets.append(t)

            
            
        return len(fleets)