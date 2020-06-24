using System;
using System.Collections.Generic;

class Program
{
    static long mod = 1000000007;

    static long pow(long x, long k, long mod) {
        k %= mod-1;
        long r = 1;
        while(k>0) {
            if((k&1)>0) r = (r*x)%mod;
            k>>=1;
            x = x*x%mod;
        }
        return r;
    }
    
    static void Main()
    {
        var str = Console.ReadLine().Split(new char[] {' '});
        long N = long.Parse(str[0]), K = long.Parse(str[1]);

        var D = new List<long>[K+1];
        for(long i=1; i<=K; ++i) D[i] = new List<long>();

        var X = new long[K+1];
        
        for(long d=1; d<=K; ++d) {
            for(long c=2; c*d<=K; ++c) D[c*d].Add(d);
            X[d] = pow(K/d, N, mod); //(K/d)**N % mod;
        }

        long ans = 0;
        for(long d=K; d>=1; --d) {
            foreach(var i in D[d]) {
                X[i] -= X[d];
                X[i] %= mod;
            }
            ans += X[d]*d%mod;
        }

        Console.WriteLine(ans%mod);

    }


}
