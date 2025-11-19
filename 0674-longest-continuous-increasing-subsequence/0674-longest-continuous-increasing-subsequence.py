class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        c = 1
        l = []
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                c+=1
            else:
                l.append(c)
                c=1
        l.append(c)    
        l.sort()
        if not l :
            return c 
        else:
            return l[-1]


        