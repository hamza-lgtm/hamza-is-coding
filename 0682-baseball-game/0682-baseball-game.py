class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = list()
        for x in operations:
            print(l)
            if x.isdecimal() or x.startswith('-') :
                l.append(int(x))
            elif x == '+':
                l.append(l[-2]+l[-1])
            elif x == 'C':
                l.remove(l[-1])
            elif x == 'D':
                l.append(l[-1]*2)
        return sum(l)

