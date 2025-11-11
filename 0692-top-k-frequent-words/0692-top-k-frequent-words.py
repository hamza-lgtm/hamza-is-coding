class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for x in words:
            d[x] = d.get(x,0)+1

        data = [(-v,k) for k,v in d.items()]
        heapq.heapify(data)
        r = []
        for i in range(k):
            value,key = heapq.heappop(data)
            r.append(key)

        return r
        