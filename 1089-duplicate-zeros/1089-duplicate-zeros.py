class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
      
        n = len(arr)
        if arr == [0]*n:
            return arr
        l,r = 0,n-1
        while l<=r:
            if arr[l] ==0:
                arr.insert(l+1,0)
                arr.pop()
                l+=1
                r+=1
    
            if r < n-1 and arr[r] == 0 and r!=l :
                arr.insert(r+1,0)
                arr.pop()
            l+=1
            r-=1
            print(l,r)
                


        