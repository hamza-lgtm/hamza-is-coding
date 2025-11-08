class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while n > nums[i] and nums[i] > 0 and nums[i] != nums[nums[i]-1]:
                t = nums[nums[i]-1]
                nums[nums[i]-1] =nums[i] 
                nums[i] = t
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
        