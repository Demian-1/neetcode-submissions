class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        ["Hello","World"]
        5:Hello5:World
        """
        res = ""
        for w in strs: 
            n = len(w)
            res = res + str(n) + ":" + w
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        print(s)
        while l < len(s):
            numS = ""
            while s[l] != ":":
                numS += s[l]
                l += 1
            n = int(numS)
            l += 1
            curr = ""
            for i in range(n):
                curr = curr + s[l]
                l = l + 1
            res.append(curr)
        return res
