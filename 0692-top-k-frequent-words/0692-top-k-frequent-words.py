class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for x in words:
            d[x] = d.get(x,0)+1

        sorted_items = sorted(d.items(), key=lambda x: (-x[1], x[0]))

        r = [x[0] for x in sorted_items[:k]]

        return r
        