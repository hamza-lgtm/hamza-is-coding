class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        i = j = 0
        r = []
        while i<n and j<m:
            if nums1[i] < nums2[j]:
                r.append(nums1[i])
                i += 1
            else:
                r.append(nums2[j])
                j += 1
        r.extend(nums1[i:])
        r.extend(nums2[j:])
        t = n + m
        mid = t//2
        if t%2==0:
            return (r[mid] + r[mid-1])/2
        else:
            return r[mid]
        
        

            


        