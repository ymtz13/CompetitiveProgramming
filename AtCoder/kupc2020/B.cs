using System;
using System.Linq;

class Program
{
    public static void Main()
    {
        var NK = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
        int N = NK[0], K = NK[1];
        long mod = 1000000007;

        var V = new long[N, K];
        for(int i=0; i<N; ++i) {
            var row = Console.ReadLine().Split(' ').Select(long.Parse).ToList();
            for(int k=0; k<K; ++k) V[i,k] = row[k];
        }
        
        var dp = new long[N, K];
        for(int k=0; k<K; ++k) dp[0,k] = 1;
        for(int i=1; i<N; ++i) {
            long s = 0;
            int j = 0;
            for(int k=0; k<K; ++k) {
                while(j<K && V[i-1,j]<=V[i,k]) {
                    s = (s + dp[i-1,j]) % mod;
                    ++j;
                }
                dp[i, k] = s;
            }
        }

        long ans = 0;
        for(int k=0; k<K; ++k) ans = (ans + dp[N-1,k]) % mod;

        Console.WriteLine(ans);
    }
}
