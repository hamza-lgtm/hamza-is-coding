class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        b = True
        i = 0
        while b and i < len(t):
            if(s.find(t[i]) == -1 ):
                b = False
            i += 1
        return b