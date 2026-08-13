class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for c in s:
            my_dict[c] = my_dict.get(c, 0) + 1
        
        for c in t:
            if c not in my_dict:
                return False
            my_dict[c] = my_dict.get(c) - 1
            if my_dict[c] == 0:
                del my_dict[c]
            
        return not my_dict