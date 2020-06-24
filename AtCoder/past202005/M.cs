using System;
using System.Collections.Generic;

class Program
{


    static int N, M, s, K;
    static List<int>[] E;
    static int[] T;
    static int[,] dist;
    static long[,] memo;
    static int[] bit;

    static int Bfs(int st, int gl)
    {
        var dist = new int[N+1];
        for(int i=0; i<N+1; ++i) dist[i] = -1;

        var queue = new List<int>(){st};
        var darray = new List<int>(){0};
        int iq = 0;
        while(iq<queue.Count && dist[gl]==-1) {
            var q = queue[iq];
            var d = darray[iq];
            iq++;

            if(dist[q]!=-1) continue;

            dist[q] = d;
            foreach(var e in E[q]) {
                queue.Add(e);
                darray.Add(d+1);
            }
        }
        
        return dist[gl];
    }

    static long Dfs(int k_st, int cities_to_visit)
    {
        if(memo[k_st,cities_to_visit]>=0) return memo[k_st, cities_to_visit];
        long retval = long.MaxValue;

        for(int k_next=0; k_next<K; ++k_next) {
            if(c)

            retval = Math.Min(retval, dist[k_st, k_next] + dfs(k_next, cities_remain));
        }
        
        return memo[k_st,cities_to_visit] = retval;
    }
    
    static void Main()
    {
        string[] buf;
        buf = Console.ReadLine().Split(" ");
        N = int.Parse(buf[0]);
        M = int.Parse(buf[1]);

        E = new List<int>[N+1];
        for(int i=0; i<N+1; ++i) E[i] = new List<int>();
        
        for(int m=0; m<M; ++m) {
            buf = Console.ReadLine().Split(" ");
            var u = int.Parse(buf[0]);
            var v = int.Parse(buf[1]);
            E[u].Add(v);
            E[v].Add(u);
        }

        s = int.Parse(Console.ReadLine());
        
        K = int.Parse(Console.ReadLine());
        memo = new long[K, 1<<K];
        for(int k=0; k<K; ++k) for(int b=0; b<(1<<K); ++b) memo[k,b] = -1;


        
        buf = Console.ReadLine().Split(" ");
        T = new int[K];
        for(int k=0; k<K; ++k) T[k] = int.Parse(buf[k]);
        
        var dist_from_s = new int[K];
        dist = new int[K, K];

        for(int k_st=0   ; k_st<K; ++k_st) {
            dist_from_s[k_st] = Bfs(s, T[k_st]);
            
            for(int k_gl=k_st; k_gl<K; ++k_gl) {
                dist[k_st, k_gl] = dist[k_gl, k_st] = Bfs(T[k_st], T[k_gl]);
            }
        }

        Console.WriteLine(dist[0, 1]);

        long ans = long.MaxValue;
        for(int k=0; k<K; ++k) {
            ans = Math.Min(ans, Dfs(k, (1<<K)-1) + dist_from_s[k]);
        }
        Console.WriteLine(ans);

        
    } // END Main

} // END Program

