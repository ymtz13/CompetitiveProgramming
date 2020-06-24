using System;

class Program
{
    static void Main()
    {
        string[] buf;
        buf = Console.ReadLine().Split(" ");
        var N = int.Parse(buf[0]);
        var S = int.Parse(buf[1]);

        buf = Console.ReadLine().Split(" ");
        var A = new long[N];
        for(int i=0; i<N; ++i) A[i] = long.Parse(buf[i]);

        long mod = 998244353L;
        
        var dp = new long[N+1, S+1];
        dp[0, 0] = 1;
        for(int i=0; i<N; ++i) {
            var a = A[i];
            for(int s=0; s<=S; ++s) {
                dp[i+1,s] = dp[i,s] * 2 % mod;
                if(s>=a) dp[i+1,s] = (dp[i+1,s] + dp[i,s-a]) % mod;
            }
        }

        Console.WriteLine(dp[N,S]);
        
    }
}
