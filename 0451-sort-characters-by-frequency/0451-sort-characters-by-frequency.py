class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        f = sorted(s,key = lambda c :(counter[c],c),reverse= True)
        return ''.join(f)
        