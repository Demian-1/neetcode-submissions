class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        lcs = 0
        for n in numsSet: 
            if n - 1 not in numsSet: 
                # start of a sequence
                ccs, cn = 1, n + 1
                while cn in numsSet: 
                    cn += 1
                    ccs += 1
                lcs = max(lcs, ccs)
            
        return lcs