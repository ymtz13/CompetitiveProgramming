using System;

class Program
{
    static int N, K;
    static int[,] T;

    static int Dfs(int i, int s) {
        if(i==N) return s;

        int min=128;
        for(int j=0; j<K; ++j) min=Math.Min(min, Dfs(i+1, s^T[i,j]));
        return min;
    }
    
    static void Main()
    {
        string[] buf;
        buf = Console.ReadLine().Split(new char[]{' '});
        N = int.Parse(buf[0]);
        K = int.Parse(buf[1]);
        T = new int[N,K];

        for(int i=0; i<N; ++i) {
            buf = Console.ReadLine().Split(new char[]{' '});
            for(int j=0; j<K; ++j) T[i,j] = int.Parse(buf[j]);
        }

        Console.WriteLine(Dfs(0, 0)==0?"Found":"Nothing");
    }
}
