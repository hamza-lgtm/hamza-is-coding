class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        p = 1
        for i in range(n):
            p^=(start + 2 * i)
        return p^1
        