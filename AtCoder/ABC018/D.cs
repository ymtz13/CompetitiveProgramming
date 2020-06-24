using System;
using System.Collections.Generic;

class Program
{
    static int N, M, P, Q;
    static int[,] Z;
    
    static int[] S;

    static int Dfs(int i, int n)
    {
        if(n>P || n+N-i<P) return 0;
        if(i==N) {
            var T = new List<int>(S);
            T.Sort();
            int retval=0;
            for(int m=0; m<Q; ++m) retval+=T[M-1-m];
            return retval;
        }

        var s0 = Dfs(i+1,n);

        for(int m=0; m<M; ++m) S[m]+=Z[i,m];
        var s1 = Dfs(i+1,n+1);
        for(int m=0; m<M; ++m) S[m]-=Z[i,m];

        return Math.Max(s0,s1);
    }
    
    static void Main()
    {
        string[] buf;
        buf = Console.ReadLine().Split(new char[]{' '});
        N = int.Parse(buf[0]);
        M = int.Parse(buf[1]);
        P = int.Parse(buf[2]);
        Q = int.Parse(buf[3]);
        var R = int.Parse(buf[4]);

        Z = new int[N, M];
        for(int i=0; i<R; ++i) {
            buf = Console.ReadLine().Split(new char[]{' '});
            var x = int.Parse(buf[0])-1;
            var y = int.Parse(buf[1])-1;
            var z = int.Parse(buf[2]);
            Z[x,y]=z;
        }

        S = new int[M];
        Console.WriteLine(Dfs(0,0));
        
    }


}
