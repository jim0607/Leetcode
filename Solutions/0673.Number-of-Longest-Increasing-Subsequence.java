Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].



class Solution {
    public int findNumberOfLIS(int[] nums) {
        // dp[i] = the number of longest increasing subseq until the ith number
        // if nums[j] > nums[i] for j>i: then dp[j] += dp[i]
        // if nums[j] < nums[i] for j > i: then dp[j] = dp[j - 1]
        
        int lens = nums.length;
        if (lens <= 1) return lens;
        
        int[] dp = new int[lens];   // dp[i]=the maxLen ended with i
        int[] cnt = new int[lens];  // cnt[i]= the cnt of maxLen ended with i
        
        for (int i = 0; i < lens; i++) {
            dp[i] = 1;
            cnt[i] = 1;
        }
        
        for (int j = 1; j < lens; j++) {
            for (int i = 0; i < j; i++) {
                if (nums[j] > nums[i]) {
                    if (dp[j] <= dp[i]) {  // first time to renew dp[j]
                        dp[j] = dp[i] + 1;
                        cnt[j] = cnt[i];
                    } else if (dp[j] == dp[i] + 1) {
                        dp[j] = dp[i] + 1;
                        cnt[j] += cnt[i];
                    }
                } 
            }
        }
        
        System.out.println(Arrays.toString(dp));
        System.out.println(Arrays.toString(cnt));
        int maxLen = 0;
        int cntofMaxLen = 0;
        for (int i = 0; i < lens; i++) {
            maxLen = Math.max(maxLen, dp[i]);
        }
        
        for (int i = 0; i < lens; i++) {
            if (dp[i] == maxLen) {
                cntofMaxLen += cnt[i];
            }
        }
        
        return cntofMaxLen;
    }
}
