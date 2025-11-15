class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        length = n.bit_length()
        for i in range(length):
            n ^= (1<<i)
        return n
        