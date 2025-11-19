class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        t = sqrt(num)
        return int(t)**2 == num
        