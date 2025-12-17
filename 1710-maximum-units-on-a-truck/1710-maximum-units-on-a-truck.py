class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        n  = len(boxTypes)
        i = 0 
        s = 0 
        r = 0 
        l= [(-boxTypes[i][1],boxTypes[i][0]) for i in range(n)]
        heapq.heapify(l)

        while i <n and s < truckSize:
            u,b = heapq.heappop(l)
            if s+b <= truckSize:
                s+=b
                r+= -b*u
            else:
                r+=-(truckSize-s)*u
                s=truckSize
            print(s,r)
            i+=1
        return r

