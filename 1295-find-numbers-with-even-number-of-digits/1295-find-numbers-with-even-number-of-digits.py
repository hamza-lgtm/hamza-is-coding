class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        c  = 0
        for x in nums:
            t = 1
            
            while x >= 10:
                
                x //= 10 
                t+=1
            if t%2 == 0:
                c+=1
        return c
            
        