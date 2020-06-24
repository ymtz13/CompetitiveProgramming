using System;
using System.Collections.Generic;

class Program
{
    static long K, N;
    static List<long>[] V;
    static string[] W;
    static long[] L;

    static void Dfs(long k)
    {
        if(k==K+1) {
            //for(int h=1; h<=K; ++h) Console.Write(L[h]);
            //Console.WriteLine();
            
            bool ok = true;
            var Z = new string[K+1];
            //var Z = new List<string>(); //new string[K+1];
            //for(int h=0; h<=K; ++h) Z.Add(null);
            
            for(long i=0; i<N && ok; ++i) {
                long st=0;
                string w = W[i];
                foreach(int p in V[i]) {
                    long l = L[p];
                    if (st+l>w.Length) {ok = false; break;}
                    string substr = w.Substring((int)st, (int)l);
                    
                    if(Z[p]==null) { Z[p]=substr; }
                    else if (Z[p]!=substr) {ok = false; break;}
                    st+=l;
                }
                if(st!=w.Length) {ok=false;}
            }

            if(ok) {
                for(int q=1; q<=K; ++q) Console.WriteLine(Z[q]);

                Environment.Exit(0);
            }
            return; 
        }
        

        for(long l=1; l<=3; ++l) {
            L[k] = l;
            Dfs(k+1);
        }

    }
    
    static void Main()
    {
        var str = Console.ReadLine().Split(new char[]{' '});
        K = long.Parse(str[0]);
        N = long.Parse(str[1]);

        V = new List<long>[N];
        W = new string[N];
        for(long i=0; i<N; ++i) {
            var str2 = Console.ReadLine().Split(new char[]{' '});
            string v = str2[0], w = str2[1];

            V[i] = new List<long>();
            for(int j=0; j<v.Length; ++j) V[i].Add(long.Parse(v[j].ToString()));
            W[i] = w;
        }

        L = new long[K+1];
        Dfs(1);

    }
}
