using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string[] buf;
        buf = Console.ReadLine().Split(new char[]{' '});
        int N = int.Parse(buf[0]),
            M = int.Parse(buf[1]);

        var E = new int[N-1, N-1];
        int INF = 1000000000;
        for(int i=0; i<N-1; ++i) for(int j=0; j<N-1; ++j) E[i,j]=(i==j ? 0:INF);
        
        var T = new List<int>();
        var U = new List<int>();
        for(int i=0; i<M; ++i) {
            buf = Console.ReadLine().Split(new char[]{' '});
            int u = int.Parse(buf[0]),
                v = int.Parse(buf[1]),
                l = int.Parse(buf[2]);

            if(u==1) { T.Add(v-2); U.Add(l); continue; }
            E[u-2, v-2] = E[v-2, u-2] = l;
        }

        for(int k=0; k<N-1; ++k)
        for(int i=0; i<N-1; ++i)
        for(int j=0; j<N-1; ++j)
            if(E[i,j]>E[i,k]+E[k,j]) E[i,j]=E[j,i]=E[i,k]+E[k,j];

        int ans = INF;
        for(int i=0;   i<T.Count; ++i)
        for(int j=i+1; j<T.Count; ++j) {
            ans = Math.Min(ans, U[i]+U[j]+E[T[i],T[j]]);
        }

        Console.WriteLine(ans==INF?-1:ans);
            
        

    }
}
