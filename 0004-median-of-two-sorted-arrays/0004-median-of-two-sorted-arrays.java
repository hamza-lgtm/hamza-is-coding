class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int m = nums2.length;
        int[] nums = new int[n+m];
        int i = 0, j = 0, k = 0;
        while(i<n && j<m){
            if(nums1[i]<nums2[j]){
                nums[k] = nums1[i];
                i++;  
            }else{
                nums[k] = nums2[j];
                j++;
            }
            k++;

        }

        while(i<n){
            nums[k] = nums1[i];
            i++;
            k++;
        }
        while(j<m){
              nums[k] = nums2[j];
              j++;
              k++;
              }
           
  
        double med ;
        int s = (n+m)/2;
        if((n+m)%2 == 0){
            med = (double) (nums[s]+nums[s-1]) / 2.0;
            
        }else{
            med =  nums[s];
        }
        return med;
        
    }
}