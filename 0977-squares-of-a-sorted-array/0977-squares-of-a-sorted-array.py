class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = []
        l,r = 0,n-1
        while l<r:
            a,b = nums[l]**2 , nums[r]**2
            if a>=b:
                result.insert(0,a)
                l+=1
                
            else:
                result.insert(0,b)
                r-=1
        result.insert(0, nums[l]**2)


        return result




        