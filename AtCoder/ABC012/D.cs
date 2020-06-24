using System;

class Program
{
    static void Main()
    {
        string[] buf;
        buf = Console.ReadLine().Split(new char[]{' '});
        var N = int.Parse(buf[0]);
        var M = int.Parse(buf[1]);

        int INF = 10000000;
        var D = new int[N,N];
        for(int i=0; i<N; ++i)for(int j=i+1; j<N; ++j) D[i,j] = D[j,i] = INF;

        for(int i=0; i<M; ++i) {
            buf = Console.ReadLine().Split(new char[]{' '});
            var a = int.Parse(buf[0]);
            var b = int.Parse(buf[1]);
            var t = int.Parse(buf[2]);
            D[a-1,b-1] = D[b-1,a-1] = t;
        }

        for(int k=0; k<N; ++k)
        for(int i=0; i<N; ++i)
        for(int j=0; j<N; ++j)
            D[i,j] = Math.Min(D[i,j], D[i,k]+D[k,j]);

        var ans = INF;
        for(int i=0; i<N; ++i) {
            int rowmax = 0;
            for(int j=0; j<N; ++j) rowmax = Math.Max(rowmax, D[i,j]);
            ans = Math.Min(ans, rowmax);
        }

        Console.WriteLine(ans);
        
    }
}
