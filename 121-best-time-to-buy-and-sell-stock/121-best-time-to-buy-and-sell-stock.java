class Solution {
    public int maxProfit(int[] prices) {
        int maxx=0;
        int val=prices[prices.length-1];
        for (int i=prices.length-2;i>=0;i--)
        {
            if (prices[i]>val)
                val=prices[i];
            else
                maxx=Math.max(maxx,val-prices[i]);
        }
        return maxx;
    }
}