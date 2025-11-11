class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            d[x] = d.get(x,0)+1

        data = [(-v,k) for k,v in d.items()]
        heapq.heapify(data)
        r = []
        for i in range(k):
            value,key = heapq.heappop(data)
            r.append(key)

        return r


            