class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}
        result = []
        for i,x in enumerate(numbers):
            c = target - x
            if c in seen.keys():
                result.append(seen[c])
                result.append(i+1)
                return result
            else:
                seen[x] = i+1

