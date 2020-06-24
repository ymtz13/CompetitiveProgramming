using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var N = int.Parse(Console.ReadLine());

        string[] buf;
        buf = Console.ReadLine().Split(new char[]{' '});

        int a = int.Parse(buf[0]),
            b = int.Parse(buf[1]);

        var M = int.Parse(Console.ReadLine());
        var E = new List<int>[N];
        for(int i=0; i<N; ++i) E[i] = new List<int>();
        for(int i=0; i<M; ++i) {
            buf = Console.ReadLine().Split(new char[]{' '});
            int x = int.Parse(buf[0]),
                y = int.Parse(buf[1]);
            E[x-1].Add(y-1);
            E[y-1].Add(x-1);
        }

        var X = new int[N];
        int mod = 1000000007;
        var queue = new List<int>{a-1};
        X[a-1]=1;
        while(queue.Count>0) {
            var queue_new = new List<int>();
            foreach(var q in queue) {
                foreach(var e in E[q]) {
                    if(X[e]==0) queue_new.Add(e);
                    if(X[e]>=0) X[e]=(X[e]-X[q])%mod;
                }
            }
            for(int i=0; i<N; ++i) if(X[i]>0) X[i]=-X[i];
            
            queue = queue_new;
        }
        Console.WriteLine(-X[b-1]);
        
    }
}
