using System;
using System.Linq;

class Program
{
    static int N, M;
    static bool[,] E;

    static bool[] X;

    static int Dfs(int i)
    {
        if(i==N) {
            bool ok = true;
            int n = 0;
            for(int p=0; p<N && ok; ++p) {
                if(X[p]) ++n;
                for(int q=p+1; q<N && ok; ++q) {
                    if(X[p] && X[q] && !E[p,q]) ok = false;
                }
            }
            return ok ? n : 0;
        }
        
        X[i] = false;
        var v0 = Dfs(i+1);
        
        X[i] = true;
        var v1 = Dfs(i+1);

        return Math.Max(v0, v1);
        
    }
    
    public static void Main()
    {
        var NM = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
        N = NM[0]; M = NM[1];

        E = new bool[N, N];
        for(int i=0; i<M; ++i) {
            var xy = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
            int x = xy[0]-1, y = xy[1]-1;
            E[x,y] = E[y,x] = true;
        }

        X = new bool[N];
        Console.WriteLine(Dfs(0));
    }
}
