class Solution:
    def removeNonAlphanumeric(self, s): 
        res = ""
        for c in s: 
            cAscii = ord(c)
            if ord('a') <= cAscii and cAscii <= ord('z'):
                res += c
            elif ord('A') <= cAscii and cAscii <= ord('Z'):
                nxt = cAscii - ord('A') + ord('a')
                res += chr(nxt)
            elif ord('0') <= cAscii and cAscii <= ord('9'):
                res += c
        
        return res

    def isPalindrome(self, s: str) -> bool:
        cleanS = self.removeNonAlphanumeric(s)
        l, r = 0, len(cleanS) - 1
        while l < r:
            if cleanS[l] != cleanS[r]:
                return False
            l += 1
            r -= 1
        return True