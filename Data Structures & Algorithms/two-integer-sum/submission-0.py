class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums = [4,5,6], target = 10

        i=0 visited={}
        dif = 10 - 4 = 6
        
        i=1 visited={{4:0}}
        dif = 10 - 5 = 5

        i=2 visited={{4:0},{5,1}}
        dif = 10 - 6 = 4

        return visited[dif],i
        """

        visited = {}
        for i, x in enumerate(nums):
            dif = target - x
            if dif in visited:
                return [visited[dif],i]
            visited[x] = i
        return [0,0]