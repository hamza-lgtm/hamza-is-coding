class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dics = {}
        for i in nums:
            dics[i] = dics.get(i,0) + 1
        a = len(nums) / 2
        for k,v in dics.items():
            if v > a:
                return k