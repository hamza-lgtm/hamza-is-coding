class Solution:
    def findComplement(self, num: int) -> int:
        r=0
        s = 0
        while num > 0:
            bit = (num & 1)^1
            r = r | (bit << s)
            num >>= 1 
            s+= 1
        return r


        