class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        d = {}
        d.setdefault(keysPressed[0],releaseTimes[0])
        for i in range(1,len(releaseTimes)):
            d[keysPressed[i]] = max (releaseTimes[i] - releaseTimes[i - 1] ,d.get(keysPressed[i],0))
        sorted_items = sorted(d.items(), key=lambda x: x[0], reverse=True)
        sorted_items = sorted(sorted_items, key=lambda x: x[1], reverse=True)
        return sorted_items[0][0]



        