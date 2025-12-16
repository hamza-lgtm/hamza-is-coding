class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(nums)
        count = sum(1 for n in s if n != 0)
        return count
       
        