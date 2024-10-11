class Solution {
    public int integerBreak(int n) {
        if (n == 2) return 1;
        if (n == 3) return 2;
        int maxProduct = 0;
        for (int i = 2; i <= n / 2 + 1; i++) {
            int quotient = n / i;
            int remainder = n % i;
            int product = (int) Math.pow(quotient, i - remainder) * (int) Math.pow(quotient + 1, remainder);
            if (product > maxProduct) {
                maxProduct = product;
            }
        }

        return maxProduct;
    }
      }  
