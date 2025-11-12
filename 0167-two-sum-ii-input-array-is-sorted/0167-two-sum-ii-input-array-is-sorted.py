class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        r = []

        for i,x in enumerate(numbers):
           
            cmp = target - x
            if cmp in list(seen.keys()):
                r.append(seen[cmp])
                r.append(i+1)
            else:
                seen[x] = i+1

        return r
            


        