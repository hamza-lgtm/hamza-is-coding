class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for s in strs:
            chars = list(s)
            chars.sort()
            k = ''.join(chars)
            d[k].append(s)

        return list(d.values())
        