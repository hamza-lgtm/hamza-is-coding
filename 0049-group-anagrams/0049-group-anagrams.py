class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for s in strs:
            chars = sorted(list(s))
            ref = ''.join(chars)
            d[ref].append(s)
        return list(d.values())