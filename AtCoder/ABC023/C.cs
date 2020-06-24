using System;

class Program
{
    static void Main()
    {
        var s1 = Console.ReadLine().Split(new char[]{' '});
        int R = int.Parse(s1[0]),
            C = int.Parse(s1[1]),
            K = int.Parse(s1[2]),
            N = int.Parse(Console.ReadLine());

        var rc = new int[N,2];
        var Nr = new int[R];
        var Nc = new int[C];        
        for(int i=0; i<N; ++i) {
            var s2 = Console.ReadLine().Split(new char[]{' '});
            int r = int.Parse(s2[0]),
                c = int.Parse(s2[1]);
            rc[i,0] = r-1;
            rc[i,1] = c-1;
            ++Nr[r-1];
            ++Nc[c-1];
        }

        var Mr = new int[N+1];
        var Mc = new int[N+1];
        for(int ir=0; ir<R; ++ir) ++Mr[Nr[ir]];
        for(int ic=0; ic<C; ++ic) ++Mc[Nc[ic]];

        long ans = 0;
        for(int nr=0; nr<=K; ++nr) {
            int nc = K-nr;
            ans += Mr[nr]*Mc[nc];
        }

        for(int i=0; i<N; ++i) {
            var ir = rc[i,0];
            var ic = rc[i,1];
            if(Nr[ir]+Nc[ic]==K  ) --ans;
            if(Nr[ir]+Nc[ic]==K+1) ++ans;
        }

        Console.WriteLine(ans);
        

    }
}
