class Solution:
    def frequencySort(self, s: str) -> str:
        counter = defaultdict()
        for c in s:
            counter[c] = counter.get(c,0)+1
        t = sorted(counter.items(),key = lambda x :(x[1],x[0]),reverse= True)
        res = ''
        for c,n in t:
            res += c*n
        return res
        