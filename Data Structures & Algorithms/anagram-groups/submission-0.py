class Solution:
    def encodeWord(self, w: str) -> str:
        code = [0] * 26
        for c in w:
            idx = ord(c) - ord('a')
            code[idx] += 1
        
        return tuple(code)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        ["act","pots","tops","cat","stop","hat"]
            "000...000"
             abc...xyz
        anagramToWord = {
            "101...000"=["act","cat"]
            "pots"=["pots","tops"]
        }
        """
        anaToWords = {}
        for w in strs: 
            code = self.encodeWord(w)
            if code in anaToWords:
                anaToWords[code].append(w)
            else:
                anaToWords[code] = [w]
        
        res = []
        for k in anaToWords:
            res.append(anaToWords[k])
        
        return res
