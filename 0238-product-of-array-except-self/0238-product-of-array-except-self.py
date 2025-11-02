class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        o = [1] * n
        p = 1
        for i in range(n):
            o[i] = p
            p *= nums[i]
        s = 1
        for i in range(n-1, -1, -1):
            o[i] *= s
            s *= nums[i]
        return o