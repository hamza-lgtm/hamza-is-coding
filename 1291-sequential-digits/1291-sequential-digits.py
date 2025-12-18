class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        r = []
        d = "123456789"

        for l in range(1,10):
            for s in range(0,10-l):
                n = int(d[s:s+l])
                if low<= n <=high:
                    r.append(n)
        return r
