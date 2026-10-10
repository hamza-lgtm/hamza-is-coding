class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1 :
            return nums[0]
        for i,x  in enumerate(nums):
            if x not in nums[:i] + nums[i+1:] :
                return x
