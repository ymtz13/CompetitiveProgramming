using System;
using System.Collections.Generic;

class Program
{

    static int ancestor(int i, int gen) {
        for(int l=1; l<20 && gen>0 && i!=-1; ++l) {
            if((gen&1)==1) i=P[l,i];
            gen>>=1;
        }
        return i;
    }

    static int[,] P;
    
    static void Main()
    {
        string[] buf;

        var N = int.Parse(Console.ReadLine());

        var E = new List<int>[N+1];
        for(int i=1; i<=N; ++i) E[i] = new List<int>();

        for(int i=0; i<N-1; ++i) {
            buf = Console.ReadLine().Split(new char[]{' '});
            var x = int.Parse(buf[0]);
            var y = int.Parse(buf[1]);
            E[x].Add(y);
            E[y].Add(x);
        }

        var D = new int[N+1];
        P = new int[20, N+1];
        for(int i=1; i<=N; ++i) P[0,i] = i;

        var queue = new List<int>(){1};
        var pqueue = new List<int>(){-1};
        int iq = 0;
        while (iq<queue.Count) {
            var q = queue[iq];
            var p = pqueue[iq];
            ++iq;

            if(P[1,q]!=0) continue;
            P[1,q] = p;
            if(q!=1) D[q]=D[p]+1;

            foreach(var e in E[q]) {
                queue.Add(e);
                pqueue.Add(q);
            }
        }

        for(int l=2; l<20; ++l) {
            for(int i=1; i<=N; ++i) {
                var p = P[l-1, i];
                P[l,i] = (p==-1 ? -1: P[l-1,p]);
            }
        }

        int Q = int.Parse(Console.ReadLine());
        for(int i=0; i<Q; ++i) {
            buf = Console.ReadLine().Split(new char[]{' '});
            var a = int.Parse(buf[0]);
            var b = int.Parse(buf[1]);
            int ans = 1+D[a]+D[b];
            a = ancestor(a, Math.Max(D[a]-D[b],0));
            b = ancestor(b, Math.Max(D[b]-D[a],0));

            int max_ng = -1, min_ok = D[a];
            int tgt = 0;
            while(min_ok-max_ng>1) {
                tgt = (min_ok+max_ng)/2;
                if(ancestor(a,tgt)==ancestor(b,tgt)) { min_ok = tgt; }
                else{ max_ng = tgt; }
            }
            ans -= 2*D[ancestor(a,min_ok)];
            
            Console.WriteLine(ans);
        }
        
    }
}
