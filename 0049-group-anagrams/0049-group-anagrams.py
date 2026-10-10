class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for s in strs:
            t = sorted(s)
            k = ''.join(t)
            d[k].append(s)
        return list(d.values())
        