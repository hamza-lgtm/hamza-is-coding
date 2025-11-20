class Solution:
    def findLHS(self, nums: List[int]) -> int:
        f = Counter(nums)
        l = 0
        for x in f:
            if x+1 in f:
                l  = max(l,f[x]+f[x+1])
        return l