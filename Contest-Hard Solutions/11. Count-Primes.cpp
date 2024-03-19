class Solution {
    public:
        int countPrimes(int n) {
            if(n <= 1) return 0;
            vector<int> dp(n+1, 1);
            dp[0] = dp[1] = 0;
            for(int i=2; i*i<=n; i++) {
                if(dp[i]) {
                    for(int j=i*i; j<=n; j+=i) {
                        dp[j] = 0;
                    }
                }
            }
            int res = 0;
            for(int i=2; i<n; i++) {
                if (dp[i]) res+=1;
            }
            return res;
        }
};