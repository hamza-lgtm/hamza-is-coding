class Solution:
    def calPoints(self, operations: list[str]) -> int:

        l = []
        

        for x in operations :
            if x == '+':
                l.append(l[-2]+l[-1])
            elif x == 'C':
                l.remove(l[-1])
            elif x == 'D':
                l.append(l[-1]*2)
            else:
                l.append(int(x))
        return sum(l)

        