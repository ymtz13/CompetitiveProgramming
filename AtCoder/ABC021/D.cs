using System;

class Program
{
    static long Pow(long x,
                   long k, long mod) {
        long r = 1;
        while(k>0) {
            if((k&1)==1) r = r*x%mod;
            x = x*x%mod;
            k>>=1;
        }
        return r;
    }

    static void Main()
    {
        var n = int.Parse(Console.ReadLine());
        var k = int.Parse(Console.ReadLine());
        int mod = 1000000007;

        var F = new long[200000];
        F[0] = 1;
        for(int i=1; i<200000; ++i) F[i] = F[i-1]*i%mod;

        long ans = F[n-1+k] * Pow(F[k], mod-2, mod) % mod;
        ans = ans * Pow(F[n-1], mod-2, mod) % mod;
        
        Console.WriteLine(ans);
    }

}
