using System;
using System.Linq;

class Program
{
    static int X = 9;
    static int XN = 1300; //1<<X; // = 512
    static int LMAX = 100000;
    static int[,] dp = new int[XN, LMAX+1];
    
    static int[,] VW;

    static int Dfs(int i, int L)
    {
        if(L<0 ) return -100000000;
        if(i<XN) return dp[i,L];

        var par = i/2;
        var v = VW[i,0];
        var w = VW[i,1];

        var v1 = Dfs(par, L);
        var v2 = Dfs(par, L-w) + v;
        
        return (v1>v2 ? v1 : v2);
    }
    
    static void Main()
    {
        var N = int.Parse(Console.ReadLine());
        VW = new int[N+1,2];
        for(int i=1; i<=N; ++i) {
            var vw = Console.ReadLine().Split().Select(int.Parse).ToArray();
            var v = VW[i,0] = vw[0];
            var w = VW[i,1] = vw[1];

            if(i<XN) {
                for(int wi=0; wi<=LMAX; ++wi) {
                    dp[i,wi] = dp[i/2,wi];
                    if(wi-w>=0) {
                        var v2 = dp[i/2, wi-w]+v;
                        if(v2>dp[i,wi]) dp[i,wi] = v2;
                    }
                }
            }
        }
        
        var Q = int.Parse(Console.ReadLine());
        for(int iq=0; iq<Q; ++iq) {
            var vL = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int v = vL[0], L = vL[1];

            Console.WriteLine(Dfs(v, L));
        }

    }
}
