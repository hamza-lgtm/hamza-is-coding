class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            d[x] = d.get(x,0)+1
        data = sorted(d.items(),key= lambda x:x[1],reverse=True)
        r = []
        for i in range(k):
            key,value =data[i]
            r.append(key)

        return r
        