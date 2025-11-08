class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d.get(c,0) + 1
        for k,v in d.items():
            if v==1:
                return s.find(k)
        return -1

        