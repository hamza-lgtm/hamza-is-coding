class Solution:
    def frequencySort(self, s: str) -> str:
        counter = defaultdict()
        for c in s:
            counter[c] = counter.get(c,0)+1
        f = sorted(s,key = lambda c :(counter[c],c),reverse= True)
        return ''.join(f)
        