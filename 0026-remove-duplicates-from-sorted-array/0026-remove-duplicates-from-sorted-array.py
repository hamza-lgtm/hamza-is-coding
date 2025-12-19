class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        v = set()
        n = len(set(nums))
        if n == 1 :
            nums = [nums[0]]
            return n
        i = 0

        while i < n :
            t = nums[i]
            if t in v:
                nums.pop(i)
            else:
                v.add(t)
                i+=1
        return n
        