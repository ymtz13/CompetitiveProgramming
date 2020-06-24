using System;
using System.Collections.Generic;

// F    1 1 2 1  2  2
// X    1 1 2 3  5  5
// S  0 1 2 4 7 12 17

class Program
{
    static void Main() {
        long mod = 1000000007;
        
        var NM = Console.ReadLine().Split(new char[]{' '});
        var N = int.Parse(NM[0]);
        var M = int.Parse(NM[1]);

        var S = new long[N+2];
        S[1]=1;

        var P = new int[M+1];
        int p=0;
        long x=0;

        for(int i=1; i<=N; ++i) {
            var f = int.Parse(Console.ReadLine());
            p = Math.Max(p,P[f]);
            P[f] = i;
            x = (S[i]-S[p]+mod)%mod;
            S[i+1]=(S[i]+x)%mod;
        }
        
        Console.WriteLine(x);
    }

}
