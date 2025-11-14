class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        result = []
        for i in range(len(nums)):
            n = nums[i]
            rest = nums[:i] + nums[i+1:]
            sub_perms = self.permute(rest)
            for perm in sub_perms:
                result.append([n] + perm)
        return result
        