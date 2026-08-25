class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}
        for i in nums:
            if i in num_to_freq:
                num_to_freq[i] += 1
            else:
                num_to_freq[i] = 1
        
        nFList = []
        for key in num_to_freq:
            nFList.append([key, num_to_freq[key]])

        nFList.sort(key=lambda e: e[1], reverse=True)

        res = []
        for n in range(k):
            res.append(nFList[n][0])

        return res

        